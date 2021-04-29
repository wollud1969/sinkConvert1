from sinkStruct import createSinkStruct
import socket
import os
from loguru import logger
import datetime
import sys
import argparse
from tick import Tick

APP_NAME = "Wollud1969 DataSink:"

version = 0x00000001
SINK_SERVER = "sink.hottis.de"
SINK_PORT = 20169

DEVICE_ID = os.environ["deviceid"]
SHARED_SECRET = os.environ["sharedsecret"]

verbose = False
oneShot = False
dummyDataSource = None




def sinkSender(frame):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(frame, (SINK_SERVER, SINK_PORT))
    sock.close()

def sanitizeFrequencyList(startTimestamp, freqList):
    # only consider timestamp down to seconds, wipe microseconds
    freqList = [ (t.replace(microsecond=0), f) for (t, f) in freqList ]

    lenFreqList = len(freqList)
    if lenFreqList > 60:
        raise ValueError("length of freqList > 60, it is {}".format(lenFreqList))
    timespan = (freqList[-1][0].replace(microsecond=0) - freqList[0][0].replace(microsecond=0)).total_seconds()
    if timespan >= 60:
        raise ValueError("timespan of freqList >= 60, it is {}".format(timespan))

    INVALID_FREQUENCY = 0
    finalTimestamp = startTimestamp
    result = []

    for (timestamp, frequency) in freqList:
        while (finalTimestamp < timestamp):
            logger.warning("{} Missing value, fill with invalid value".format(APP_NAME))
            finalTimestamp += datetime.timedelta(seconds=1)
            result.append(INVALID_FREQUENCY)
        result.append(int(frequency * 1000))
        finalTimestamp += datetime.timedelta(seconds=1)

    while len(result) < 60:
        result.append(INVALID_FREQUENCY)

    return result


def init():
    argParser = argparse.ArgumentParser(
        description="Wollud1969 DataSink: SinkConvert1",
        epilog="""
When not using dummy data, the MongoDB module requires the environment 
variables 'serveruser', 'serverpassword' and 'server_url'.
The sink sender in any case requires the env variables 'deviceid' and
'sharedsecret'.        
        """
    )
    argParser.add_argument('--verbose', '-v',
                        help='verbose output',
                        required=False,
                        action='store_true',
                        default=False)
    argParser.add_argument('--oneShot', '-o',
                        help='run once and terminate',
                        required=False,
                        action='store_true',
                        default=False)
    argParser.add_argument('--dummyDataSource', '-d',
                        help='select dummy data source, current 1, 2 or 3',
                        required=False,
                        default=None)
    args = argParser.parse_args()

    global verbose, oneShot, dummyDataSource
    verbose = args.verbose
    oneShot = args.oneShot
    dummyDataSource = args.dummyDataSource


# ---- MAIN ---------------------------------------------------------

init()


if dummyDataSource == "1":
    from getDummyData import getData
elif dummyDataSource == "2":
    from getDummyData2 import getData
elif dummyDataSource == "3":
    from getDummyData3 import getData
else:
    from getData import getData

tick = None
if not oneShot:
    tick = Tick(60)
    tick.start()

while True:
    started_at = datetime.datetime.now()

    try:
        startTime = datetime.datetime.utcnow().replace(microsecond=0) - datetime.timedelta(minutes=5)
        timestampFrequencyTuples = getData(startTime)
        logger.debug("{} Gathered data: {} {}".format(APP_NAME, len(timestampFrequencyTuples), timestampFrequencyTuples))

        sanitizedFrequencyList = sanitizeFrequencyList(startTime, timestampFrequencyTuples)
        logger.debug("{} Sanitized frequencies: {} {}".format(APP_NAME, len(sanitizedFrequencyList), sanitizedFrequencyList))

        frame = createSinkStruct(DEVICE_ID, SHARED_SECRET, 
                                 version, startTime, sanitizedFrequencyList)
        logger.debug("{} Data for sink: {} {}".format(APP_NAME, len(frame), (' '.join(format(x, '02x') for x in frame))))

        sinkSender(frame)
        logger.info("{} Data sent to sink".format(APP_NAME))
    except Exception as e:
        logger.error("{} Exception: {}, {}".format(APP_NAME, e.__class__.__name__, e))

    ended_at = datetime.datetime.now()
    duration_ms = (ended_at - started_at) / datetime.timedelta(milliseconds=1)
    logger.info("{} Duration: {} ms".format(APP_NAME, duration_ms))

    if oneShot:
        break
    else:
        tick.waitForTick()

