from socket import *
import struct


class Finder(object):
    def __init__(self):
        self.multicast_group = ('224.1.1.1', 5000)
        self.message = 'hello world'
        self.enc = 'utf-8'
        self.send_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.send_socket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
        self.rec_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.rec_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.rec_socket.bind(('', self.multicast_group[1]))
        mreq = struct.pack("4s4s", inet_aton(self.multicast_group[0]), inet_aton('0.0.0.0'))
        self.rec_socket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

    def multicast_send(self):
        send_message = self.message.encode(self.enc)
        self.send_socket.sendto(send_message, self.multicast_group)

    def multicast_receive(self):
        data, addr = self.rec_socket.recvfrom(1024)
        print(data.decode(self.enc))



f = Finder()
print('1')
while(1):
    f.multicast_send()
    f.multicast_receive()
    
