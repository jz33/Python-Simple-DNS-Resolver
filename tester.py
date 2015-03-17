import DNSMessage
import DNSResolver
import struct

question = 'google.com'
rr = 'MX'
ACK = chr(6)

data = DNSMessage.Header() + ACK + DNSMessage.Question(question,rr)
for w in data: print ord(w),
print

resolver = DNSResolver.Resolver(data = data)
resolver.Connect()
resolver.Send()
try:
    chunk = resolver.Receive()
    DNSMessage.Answer(chunk)
finally:
    resolver.Disconnect()
    

    

