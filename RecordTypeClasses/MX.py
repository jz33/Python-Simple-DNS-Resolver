import Base
import struct

class MX(Base.Base):

    def __init__(self):
        self.preference = Base.UNDEFINED
        self.exchange   = Base.UNDEFINED
        
    def Decode(self, msg, curr, rdlen):
        (preference, ) = struct.unpack('!H', msg[curr : curr + 2])
        (exchange, _) = Base.ReadName(msg,curr + 2)
        self.preference = preference
        self.exchange   = exchange
        return curr + rdlen
        
    def __str__(self):
        return 'Host: %s Preference: %d\n' % (self.exchange,self.preference)
    