import DNSRecordTypes
import DNSClassLoader
from RecordTypeClasses.Base import ReadName

import random
import struct
import threading
'''
DNS Message Processor
Author: junzhengrice@gmail.com
'''
def Header():
    """
    http://www.zytrax.com/books/dns/ch15/#header
    Return DNS message header
    
    @rtype: string
    """
    lock = threading.Lock()
    lock.acquire()
    counts = [0 for i in xrange(0,4)]
    
    try:
        # Message ID
        id = random.randint(1,255)
        id <<= 8
        id += random.randint(1,255)
    
        # QR OPCODE AA TC RD RA res1 res2 res3 RCODE
        flags = 1
        flags <<= 8
    
        # QDCOUNT
        counts[0] = 1
    
        # ANCOUNT
    
        # NSCOUNT
    
        # ARCOUNT
       
    finally:
        lock.release()
    return struct.pack('!HHHHHH',id,flags,counts[0],counts[1],counts[2],counts[3])
    
def Question(ques,rr):
    """
    http://www.zytrax.com/books/dns/ch15/#question
    Return DNS question
    
    domain:
    www.google.com -> www 08 google 03 com

    @rtype: string
    """
    lock = threading.Lock()
    lock.acquire()
    ret = ques
    try:
        # QNAME
        pos = ret.find('www')
        if pos != -1:
            ret[pos+1] = chr(8)
        ret = ret.replace('.',chr(3),1)
        
        # NULL
        ret += chr(0)
        
        # QTYPE
        ret += chr(0)
        if isinstance(rr, (str, unicode)):
            ret += chr(DNSRecordTypes.toInt(rr))
        elif isinstance(rr, int):
            ret += chr(rr)
        else:
            raise TypeError
             
        # QCLASS
        ret += chr(0)
        ret += chr(1)
        
    finally:
        lock.release()
    return ret

def Answer(msg):
    '''
    http://www.zytrax.com/books/dns/ch15/#answer
    Return DNS answer
    '''
    if len(msg) < 12:
        raise IndexError
  
    counts = [0 for i in xrange(0,4)]
    (id, flags, counts[0], counts[1], counts[2], counts[3]) =\
         struct.unpack('!HHHHHH', msg[:12])

    curr = 12
    
    # QUESTION
    for i in xrange(counts[0]):
        (text, used) = ReadName(msg, curr)
        curr += used
        (rdtype, rdclass) = struct.unpack('!HH', msg[curr : curr+4])
        curr = curr + 4
        #print i, 'QUESTION: ', text, used, rdtype, rdclass
    
    # ANSWER
    for i in xrange(counts[1]):
        (text, used) = ReadName(msg, curr)
        curr += used
        (rdtype, rdclass, ttl, rdlen) = struct.unpack('!HHIH',msg[curr:curr+10])
        curr = curr + 10
 
        rrTypeName = DNSRecordTypes.toStr(rdtype)
        mod = DNSClassLoader.LoadClass(rrTypeName)
        answerClass = getattr(mod, rrTypeName)()
        curr = answerClass.Decode(msg,curr,rdlen)
        print answerClass
        
    # AUTHORITY
    
    # ADDITIONAL
    