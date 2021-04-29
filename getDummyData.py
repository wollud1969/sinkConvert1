from loguru import logger
import datetime
import random

def getData(startTimestamp):
    # raise ValueError("Test Dummy Error")

    endTimestamp = startTimestamp + datetime.timedelta(seconds=60)

    # dummy implementation
    result = []
    timestamp = startTimestamp
    while (timestamp < endTimestamp):
        frequency = 50.0 + random.randrange(-99,99)/1000
        result.append((timestamp, frequency))
        timestamp += datetime.timedelta(seconds=1)
    
    logger.debug("Wollud1969 DataSink: Dummy data Set 1 provided")
    return result
