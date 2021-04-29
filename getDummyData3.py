from loguru import logger
import datetime
import random

def getData(startTimestamp):
    endTimestamp = startTimestamp + datetime.timedelta(seconds=60)

    data = []
    data.append(((startTimestamp + datetime.timedelta(seconds=0)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=1)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=2)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=3)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=4)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=5)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=6)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=7)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=8)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=9)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=10)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=11)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=12)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=13)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=14)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=15)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=16)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=17)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=18)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=19)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=20)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=21)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=22)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=23)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=24)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=25)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=26)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=27)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=28)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=29)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=30)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=31)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=32)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=33)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=34)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=35)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=36)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=37)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=38)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=39)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=40)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=41)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=42)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=43)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=44)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=45)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=46)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=47)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=48)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=49)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=50)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=51)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=52)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=53)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=54)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=55)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=56)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=57)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=59)), (50.0 + random.randrange(-99,99)/1000)))
    data.append(((startTimestamp + datetime.timedelta(seconds=60)), (50.0 + random.randrange(-99,99)/1000)))
   
    logger.debug("Wollud1969 DataSink: Dummy data Set 2 provided")
    return data
