import DNSMessage
import DNSResolver
import struct

ACK = chr(6)

def composeData(question, rr):
    data = DNSMessage.Header() + ACK + DNSMessage.Question(question,rr) 
    for w in data: print ord(w),
    print
    return data    


def execute(resolver,question,type):
    data = composeData(question,type)
    resolver.UpdateData(data)
    resolver.Send()
    chunk = resolver.Receive()
    DNSMessage.Answer(chunk)
    print
        
def main():
    question = 'google.com'
    
    resolver = DNSResolver.Resolver()
    resolver.Connect()
    try:
        execute(resolver,question,'A')
        execute(resolver,question,'MX')
    finally:
        resolver.Disconnect()
        
if __name__ == '__main__':
    main()
