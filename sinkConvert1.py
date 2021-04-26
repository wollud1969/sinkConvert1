from sinkStruct import createSinkStruct
import socket
import os
from loguru import logger
import datetime
import sys
import argparse
import threading


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
    argParser = argparse.ArgumentParser(description="SinkConvert1")
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


while True:
    startTime = datetime.datetime.utcnow().replace(microsecond=0) - datetime.timedelta(minutes=5)
    timestampFrequencyTuples = getData(startTime)
    logger.debug("Gathered data: {}".format(timestampFrequencyTuples))

    sanitizedFrequencyList = sanitizeFrequencyList(startTime, timestampFrequencyTuples)
    logger.debug("Sanitized frequencies: {} {}".format(len(sanitizedFrequencyList), sanitizedFrequencyList))

    frame = createSinkStruct(DEVICE_ID, SHARED_SECRET, 
                             version, startTime, sanitizedFrequencyList)
    logger.debug("Data for sink: {} {}".format(len(frame), (' '.join(format(x, '02x') for x in frame))))

    sinkSender(frame)
    logger.info("Data sent to sink")

    if oneShot:
        break

    with cond:
        cond.wait()


