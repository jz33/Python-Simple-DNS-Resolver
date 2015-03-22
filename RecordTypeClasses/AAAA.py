import Base
import struct

class AAAA(Base.Base):
    def __init__(self):
        self.address = Base.UNDEFINED
        
    def Decode(self, msg, curr, rdlen):
        if rdlen != 16:
            raise IndexError
            
        hex = msg[curr:curr+rdlen].encode('hex_codec')
        hex.lstrip('0')
        self.address = ''
        for i in range(0,4):
            sub = hex[i*4 : (i+1)*4]
            sub = sub.lstrip('0')
            if len(sub) == 0: sub = '0'
            self.address += sub
            self.address += ':'
        self.address += ':'
        sub = hex[16:].lstrip('0')
        self.address += sub
        return curr + rdlen

    def __str__(self):
        return "IPv6 address: %s" % (self.address)
    
