'''
DNS resouce record types base class
Author: junzhengrice@gmail.com
'''

UNDEFINED = 'UNCOMPUTED VALUE'

def ReadName(msg, curr):
    labels = []
    hops = 0
    count = ord(msg[curr])
    curr += 1
    used = 1
    while count != 0:
        if count < 64:
            labels.append(msg[curr : curr + count])
            curr += count
            if hops == 0: used += count
        elif count >= 192:
            curr = ((count & 0x3f) << 8) + ord(msg[curr])
            if hops == 0: used += 1
            hops += 1
        else:
            print os.path.basename(__file__), ' count is out of bound.'
            raise 
            
        count = ord(msg[curr])
        curr += 1
        if hops == 0: used += 1
    labels.append('')
    return ('.'.join(labels),used)
    
class Base(object):
    def __init__(self):
        pass
        
    def Decode(self,msg, curr):
        pass
        
    def __str__(self):
        pass