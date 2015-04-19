import Base
import struct

class SOA(Base.Base):  
    def __init__(self):
        self.primary = Base.UNDEFINED
        self.admin = Base.UNDEFINED
 
    def Decode(self, msg, curr, rdlen):
        (self.primary,used) = Base.ReadName(msg,curr)
        curr += used
        (self.admin,used) = Base.ReadName(msg,curr)
        curr += used
        
        left = struct.unpack('!IIIII',msg[curr:curr+20])
        self.serial = left[0]
        self.refresh = left[1]
        self.retry = left[2]
        self.expiration = left[3]
        self.minimum = left[4]
                                    
        return curr + rdlen

    def __str__(self):        
        return 'Primary NS: %s\n\
Admin MB: %s\n\
Serial Number: %d\n\
Refresh Interval: %d\n\
Retry Interval: %d\n\
Expiration Limit: %d\n\
Minimum TTL: %d' \
% (self.primary,self.admin,self.serial,self.refresh,\
self.retry,self.expiration,self.minimum)
        
     
