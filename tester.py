import DNSMessage
import DNSResolver

DEBUG = False

def execute(resolver,question,rr):
    data = DNSMessage.Header() + DNSMessage.Question(question,rr)
    
    if DEBUG:
        for w in data: print ord(w),
        print
    
    resolver.UpdateData(data)
    resolver.Send()
    chunk = resolver.Receive()
    DNSMessage.Answer(chunk)
    print
        
def main():
    question = 'wikipedia.org'
    question = 'google.com'
    
    resolver = DNSResolver.Resolver()
    resolver.Connect()
    try:
        execute(resolver,question,'A')
        execute(resolver,question,'NS')
        execute(resolver,question,'MX')
        execute(resolver,question,'SOA')
        execute(resolver,question,'TXT')
        execute(resolver,question,'AAAA')
        
    finally:
        resolver.Disconnect()
        
if __name__ == '__main__':
    main()
