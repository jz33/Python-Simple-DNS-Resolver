import socket
import sys
import os
import struct
'''
DNS Resolver
Author: junzhengrice@gmail.com
'''
def GetNameServers():
    '''
    Pick only IPv4 name servers
    '''
    nameservers = []
    try:
        f = open('/etc/resolv.conf', 'r')
    except IOError:
        nameservers = ['127.0.0.1']
        needToClose = True
    else:
        needToClose = False
        
    for line in f:
        if len(line) == 0 or line[0] == '#' or line[0] == ';':
            continue
        tokens = line.split()
        if len(tokens) == 0: 
            continue
        if tokens[0] == 'nameserver':
            if not '::' in tokens[1]:
                nameservers.append(tokens[1])
                
    if needToClose: f.close()    
    if len(nameservers) == 0: nameservers.append('127.0.0.1') 
    return nameservers
    
class Resolver:
    def __init__(self, data = '', sock = None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.data = data
        self.tcpmsg = struct.pack("!H", len(self.data)) + self.data

    def Connect(self, nameserver = None):
        if nameserver is None:
            nameserver = GetNameServers()[0]
        self.sock.connect((nameserver,53))

    def Disconnect(self):
        self.sock.close()
        
    def Send(self):
        totalsent = 0
        while totalsent < len(self.tcpmsg):
            sent = self.sock.send(self.tcpmsg[totalsent:])
            if sent == 0:
                print os.path.basename(__file__), ' socket send failed'
                raise 
            totalsent += sent
    
    def Receive(self):
        ldata = self.sock.recv(2)
        if ldata == '':
            print os.path.basename(__file__), ' socket receive failed'
            raise
        (recvLen,) = struct.unpack("!H", ldata)
        
        chunks = []
        bytes_recd = 0
        while bytes_recd < recvLen:
            chunk = self.sock.recv(min(recvLen - bytes_recd, 2048))
            if chunk == '':
                print os.path.basename(__file__), ' socket receive failed'
                raise
            chunks.append(chunk)
            bytes_recd += len(chunk)
        return ''.join(chunks)       