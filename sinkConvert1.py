from sinkStruct import createSinkStruct
from getData import getData
import socket
import os
import time


def sinkSender(frame):
    SINK_SERVER = "sink.hottis.de"
    SINK_PORT = 20169

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(frame, (SINK_SERVER, SINK_PORT))
    sock.close()

def sanitizeFrequencyList(startTimestamp, freqList):
    INVALID_FREQUENCY = 0
    finalTimestamp = startTimestamp
    result = []

    for freqTuple in freqList:
        (timestamp, frequency) = freqTuple
        if timestamp == finalTimestamp:
            result.append(int(frequency * 1000))
        else:
            while (finalTimestamp < timestamp):
                finalTimestamp += 1
                result.append(INVALID_FREQUENCY)
        finalTimestamp += 1
    
    return result


# 16 octets
deviceId = os.environ['sinkDeviceId']

# 32 octets
sharedSecret = os.environ['sinkSharedSecret']

# uptime in hours, version, each 4 octets
uptime = int(time.clock_gettime(time.CLOCK_BOOTTIME) / 3600)
version = 0xcafebabe

startTime = int(time.clock_gettime(time.CLOCK_REALTIME))
timestampFrequencyTuples = getData(startTime, startTime + 60)
print(timestampFrequencyTuples)
sanitizedFrequencyList = sanitizeFrequencyList(startTime, timestampFrequencyTuples)
print(sanitizedFrequencyList)
print(len(sanitizedFrequencyList))
frame = createSinkStruct(deviceId, sharedSecret, uptime, version, 
                         startTime, sanitizedFrequencyList)

print(frame)
print(len(frame))

sinkSender(frame)