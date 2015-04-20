'''
DNS Record types
http://en.wikipedia.org/wiki/List_of_DNS_record_types
'''
NONE = 0
A = 1
NS = 2
CNAME = 5
SOA = 6
WKS = 11
PTR = 12
MX = 15
TXT = 16
AAAA = 28
A6 = 38
ANY = 255

DictStrToInt = {
    'NONE' : NONE,
    'A' : A,
    'NS' : NS,
    'CNAME' : CNAME,
    'SOA' : SOA,
    'WKS' : WKS,
    'PTR' : PTR,
    'MX' : MX,
    'TXT' : TXT,
    'AAAA' : AAAA,
    'A6' : A6,
    'ANY' : ANY,
    }

DictIntToStr = {
    NONE : 'NONE',
    A : 'A',
    NS : 'NS',
    CNAME : 'CNAME',
    SOA : 'SOA',
    WKS : 'WKS',
    PTR : 'PTR',
    MX : 'MX',
    TXT : 'TXT',
    AAAA : 'AAAA',
    A6 : 'A6',
    ANY : 'ANY',
    }
    
def toInt(text):
    value = DictStrToInt.get(text.upper())
    if value is None:
        raise LookupError
    return value
    
def toStr(id):
    value = DictIntToStr.get(id)
    if value is None:
        raise LookupError
    return value

