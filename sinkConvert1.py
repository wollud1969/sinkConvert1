from sinkStruct import createSinkStruct
from getData import getData
import socket
import os
import datetime
import configparser
import logging as log
import sys
import argparse


config = None
version = 0x00000001


def sinkSender(frame):
    global config
    sinkServer = config['SINK']['Server']
    sinkPort = int(config['SINK']['Port'])

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(frame, (sinkServer, sinkPort))
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
    global config
    argParser = argparse.ArgumentParser(description="SinConvert1")
    argParser.add_argument('--verbose', '-v',
                        help='verbose output',
                        required=False,
                        action='store_true',
                        default=False)
    argParser.add_argument('--configFile', '-c',
                        help='configFile', required=False,
                        default='./sinkConvert1.cfg')
    args = argParser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.configFile)
    if args.verbose:
        config['GLOBAL']['Verbose'] = 'true'

    logHandlers = [ log.FileHandler(filename=config['GLOBAL']['Logfile']) ]
    if config['GLOBAL']['Verbose'].upper() in ['TRUE', 'YES']:
        logHandlers.append(log.StreamHandler(sys.stdout))
    log.basicConfig(level=log.DEBUG, handlers=logHandlers,
                    format='%(asctime)s %(levelname)s : %(message)s')



# ---- MAIN ---------------------------------------------------------

init()


startTime = datetime.datetime.utcnow().replace(microsecond=0)
timestampFrequencyTuples = getData(config['SOURCE'], startTime)
log.debug("Gathered data: {}".format(timestampFrequencyTuples))

sanitizedFrequencyList = sanitizeFrequencyList(startTime, timestampFrequencyTuples)
log.debug("Sanitized frequencies: {} {}".format(len(sanitizedFrequencyList), sanitizedFrequencyList))

frame = createSinkStruct(config['SINK']['DeviceId'], config['SINK']['SharedSecret'], 
                         version, startTime, sanitizedFrequencyList)
log.debug("Data for sink: {} {}".format(len(frame), (' '.join(format(x, '02x') for x in frame))))

sinkSender(frame)
log.info("Data sent to sink")