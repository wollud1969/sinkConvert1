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
dummyData = False




def sinkSender(frame):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(frame, (SINK_SERVER, SINK_PORT))
    sock.close()

def sanitizeFrequencyList(startTimestamp, freqList):
    INVALID_FREQUENCY = 0
    finalTimestamp = startTimestamp
    result = []

    for (timestamp, frequency) in freqList:
        while (finalTimestamp < timestamp):
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
    argParser.add_argument('--dummyData', '-d',
                        help='use dummy data',
                        required=False,
                        action='store_true',
                        default=False)
    args = argParser.parse_args()

    global verbose, oneShot, dummyData
    verbose = args.verbose
    oneShot = args.oneShot
    dummyData = args.dummyData


# ---- MAIN ---------------------------------------------------------

init()


if dummyData:
    from getDummyData import getData
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
        logger.debug("{} Gathered data: {}".format(APP_NAME, timestampFrequencyTuples))

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

