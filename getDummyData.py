from loguru import logger
import datetime

def getData(startTimestamp):
    # raise ValueError("Test Dummy Error")

    endTimestamp = startTimestamp + datetime.timedelta(seconds=60)

    # dummy implementation
    result = []
    timestamp = startTimestamp
    frequency = 50.0
    while (timestamp < endTimestamp):
        result.append((timestamp, frequency))
        timestamp += datetime.timedelta(seconds=1)
    
    logger.debug("Wollud1969 DataSink: Dummy data provided")
    return result
