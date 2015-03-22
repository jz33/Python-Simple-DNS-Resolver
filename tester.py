import DNSMessage
import DNSResolver
import struct

def execute(resolver,question,rr):
    data = DNSMessage.Header() + DNSMessage.Question(question,rr)
    
    for w in data: print ord(w),
    print
    
    resolver.UpdateData(data)
    resolver.Send()
    chunk = resolver.Receive()
    DNSMessage.Answer(chunk)
    print
        
def main():
    #question = 'google.com'
    question = 'wikipedia.org'
    
    resolver = DNSResolver.Resolver()
    resolver.Connect()
    try:
        execute(resolver,question,'A')
        execute(resolver,question,'MX')
        execute(resolver,question,'NS')
    finally:
        resolver.Disconnect()
        
if __name__ == '__main__':
    main()
