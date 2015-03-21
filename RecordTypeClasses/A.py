import Base
import struct

class A(Base.Base):

    def __init__(self):
        self.address = Base.UNDEFINED
        
    def Decode(self, msg, curr, rdlen):
        if rdlen != 4:
            raise IndexError
        self.address  = msg[curr:curr+rdlen]
        return curr + rdlen

    def __str__(self):
        return 'IPv4 address: %u.%u.%u.%u' % (ord(self.address[0]), \
            ord(self.address[1]), ord(self.address[2]), \
            ord(self.address[3]))
    
