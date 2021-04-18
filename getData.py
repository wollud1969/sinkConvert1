def getData(startTimestamp, endTimestamp):
    """
    This function collects data from the database.
    It returns data with a timestamp greater or equal
    startTimestamp and less (without equal!) endTimestamp.
    It returns this data as an array of arrays. The 
    inner arrays are always two-tuples with the timestamp
    in UNIX seconds in UTC on position 0 and the frequency
    in Hz as float on position 1.
    The timestamps in the list have to be monotonic raising.
    """

    # dummy implementation
    result = []
    timestamp = startTimestamp
    frequency = 50.0
    while (timestamp < endTimestamp):
        result.append([timestamp, frequency])
        timestamp += 2
    
    return result
