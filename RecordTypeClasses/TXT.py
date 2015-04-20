import Base

class TXT(Base.Base):

    def __init__(self):
        self.info = Base.UNDEFINED
        
    def Decode(self, msg, curr, rdlen):
        size = ord(msg[curr])
        self.info = msg[curr+1 : curr+1+size]
        return curr + len(msg)

    def __str__(self):
        return "Txt record: "+self.info
    
