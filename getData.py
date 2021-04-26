import os
from datetime import timedelta
from urllib.parse import quote_plus

import pandas as pd
from bson.codec_options import CodecOptions
from loguru import logger
from pandas import json_normalize
from pymongo import MongoClient

uri = "mongodb://%s:%s@%s" % (
    quote_plus(os.environ["serveruser"]), quote_plus(os.environ["serverpassword"]),
    quote_plus(os.environ["server_url"]))
client = MongoClient(uri)
measurements_db = client.gridfrequency.get_collection('measurement', codec_options=CodecOptions(tz_aware=True))


def get_data(startTimestamp):
    """
    This function collects data from the database.

    It returns data with a timestamp greater or equal
    startTimestamp and less (without equal!) endTimestamp (computed below).

    It returns this data as an list of lists. The inner lists are always 
    two-tuples with the timestamp as datetime object in UTC on position 0 and 
    the frequency in Hz as float on position 1.
    The timestamps in the list have to be monotonic raising.
    There must be no more then one tuple per second.
    If for a particular second no value is available it shall be skipped.
    
    So, as the end time (see below) is 60 seconds after the start time, there
    must no be more then 60 tuples in the result.

    Use log.info, log.debug, log.warning, ... for logging.
    Use the dictionary config for your configuration. Enter the required
    parameters in the configuration file in the section SOURCE.
    """

    endTimestamp = startTimestamp + timedelta(seconds=60)

    def query_db(start, stop):
        try:
            cursor = measurements_db.aggregate(pipeline=[
                {"$match": {"first": {"$lt": stop}, "last": {"$gt": start}}},
                {"$match": {"data.t": {"$lt": stop}, "data.t": {"$gt": start}}},
                {"$unwind": "$data"},
                {"$group": {"_id": "$data.t", "t": {"$first": "$data.t"}, "f": {"$first": "$data.f"}}},
            ])
            data = json_normalize(cursor).drop(["_id"], axis=1)
            data = data[data["t"] <= stop]
            data = data[data["t"] >= start]
            data = data.set_index("t").sort_index()
        except Exception as e:
            logger.error("Wollud1969 DataSink: DB access failed.")
            raise ValueError("Could not get data from database")
        return data

    startTimestamp = startTimestamp
    endTimestamp = endTimestamp
    data = query_db(startTimestamp, endTimestamp).reset_index()
    data["t_d"] = pd.to_datetime(data['t'], utc=True)
    mean = data.set_index("t_d")["f"].rolling("1s").mean()
    secondOfHour = mean.index.minute * 60 + mean.index.second
    data["secondOfHour"] = secondOfHour
    data = data.drop_duplicates(subset="secondOfHour", keep="first")
    data = data.drop(columns=["secondOfHour", "t_d"])
    return data.values.tolist()
