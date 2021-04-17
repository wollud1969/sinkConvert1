from sinkStruct import createSinkStruct
import socket
import os

def sinkSender(frame):
    SINK_SERVER = "sink.hottis.de"
    SINK_PORT = 20169

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(frame, (SINK_SERVER, SINK_PORT))
    sock.close()



# 16 octets
deviceId = os.environ['sinkDeviceId']

# 32 octets
sharedSecret = os.environ['sinkSharedSecret']

# uptime, version, each 4 octets
uptime = 100
version = 0xcafebabe

# timestamp in UNIX seconds, UTC, 8 octets
timestamp = 1600000000

freqs = [ 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000, 
    50000, 50000, 50000, 50000, 50000
]

frame = createSinkStruct(deviceId, sharedSecret, uptime, version, timestamp, freqs)

print(frame)
print(len(frame))

sinkSender(frame)