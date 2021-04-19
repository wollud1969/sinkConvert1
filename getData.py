import logging as log

def getData(config, startTimestamp):
    """
    This function collects data from the database.

    It returns data with a timestamp greater or equal
    startTimestamp and less (without equal!) endTimestamp (computed below).

    It returns this data as an array of arrays. The inner arrays are always 
    two-tuples with the timestamp in UNIX seconds in UTC on position 0 and 
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


    endTimestamp = startTimestamp + 60

    # dummy implementation
    result = []
    timestamp = startTimestamp
    frequency = 50.0
    while (timestamp < endTimestamp):
        result.append([timestamp, frequency])
        timestamp += 1
    
    log.debug("Dummy data provided")
    return result
