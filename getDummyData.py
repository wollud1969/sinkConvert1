from loguru import logger
import datetime

def getData(startTimestamp):
    endTimestamp = startTimestamp + datetime.timedelta(seconds=60)

    # dummy implementation
    result = []
    timestamp = startTimestamp
    frequency = 50.0
    while (timestamp < endTimestamp):
        result.append((timestamp, frequency))
        timestamp += datetime.timedelta(seconds=1)
    
    logger.debug("Dummy data provided")
    return result
