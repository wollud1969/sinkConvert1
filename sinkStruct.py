from hashlib import sha256


class ext_bytearray_exception(Exception): pass

class ext_bytearray(bytearray):
    def appendInt32(self, v):
        vv = v.to_bytes(4, 'little')
        self.append(vv[0])
        self.append(vv[1])
        self.append(vv[2])
        self.append(vv[3])

    def appendInt64(self, v):
        vv = v.to_bytes(8, 'little')
        self.append(vv[0])
        self.append(vv[1])
        self.append(vv[2])
        self.append(vv[3])
        self.append(vv[4])
        self.append(vv[5])
        self.append(vv[6])
        self.append(vv[7])

    def appendFixedLengthString(self, v, length):
        if len(v) > length:
            raise ext_bytearray_exception()
        self.extend(v.encode())
        self.extend(('\0'*(length - len(v))).encode())

    
def createSinkStruct(deviceId, sharedSecret, uptime, version, timestamp, frequencyArray):
    if len(frequencyArray) != 60:
        raise ext_bytearray_exception()

    buffer = ext_bytearray()

    buffer.appendFixedLengthString(deviceId, 16)
    buffer.appendFixedLengthString(sharedSecret, 32)

    buffer.appendInt32(uptime)
    buffer.appendInt32(0)
    buffer.appendInt32(0)
    buffer.appendInt32(version)

    buffer.appendInt64(timestamp)

    for f in frequencyArray:
        buffer.appendInt32(f)

    h = sha256()
    h.update(buffer)
    aux = h.digest()

    for idx, val in enumerate(aux):
        buffer[16 + idx] = aux[idx]

    return buffer



