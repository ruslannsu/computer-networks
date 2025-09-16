import struct
import time 
from socket import *
from threading import *


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
        while(True):
            send_message = self.message.encode(self.enc)
            self.send_socket.sendto(send_message, self.multicast_group)
            time.sleep(1)

    def multicast_receive(self):
        while(True):
            data, addr = self.rec_socket.recvfrom(1024)
            print(data.decode(self.enc))
            print(addr)
            time.sleep(1)


    def run(self):
        rec_thread = Thread(target=self.multicast_receive)
        send_thread = Thread(target=self.multicast_send)
        rec_thread.start()
        send_thread.start()


f = Finder()
f.run()