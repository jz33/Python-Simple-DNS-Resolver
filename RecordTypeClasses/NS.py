import Base
import struct

class NS(Base.Base):

    def __init__(self):
        self.target = Base.UNDEFINED
        
    def Decode(self, msg, curr, rdlen):
        (self.target,_ ) = Base.ReadName(msg,curr)
        return curr + rdlen

    def __str__(self):
        return 'NS target: %s' % (self.target)
    
