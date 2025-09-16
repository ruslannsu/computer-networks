import struct
import time 
from socket import *
from threading import *
from collections import deque

import collections
class Finder(object):
    def __init__(self):
        self.multicast_group = ('224.1.1.1', 5000)
        self.message = '12242232'
        self.enc = 'utf-8'
        self.send_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.send_socket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
        self.rec_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.rec_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.rec_socket.bind(('', self.multicast_group[1]))
        mreq = struct.pack("4s4s", inet_aton(self.multicast_group[0]), inet_aton('0.0.0.0'))
        self.rec_socket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
        self.dict = {}
        self.time_offset = 5
        

    def clean(self):
        time_ = int(time.time())
        for key, value in list(self.dict.items()):
            if (time_ - value > self.time_offset):
                self.dict.pop(key)
                print(f"{key} died")


     
    def screen(self):
        for _, value in self.dict.items():
            print('alive:')
            print(value)    
        
            
        


    def run(self):
        self.screen()
        while (True):
            send_message = self.message.encode(self.enc)
            self.send_socket.sendto(send_message, self.multicast_group)
            message, address = self.rec_socket.recvfrom(1024)
            message = message.decode(self.enc)
            if (message != self.message):
                continue
            self.dict[address] = time.time()
            time.sleep(1)
            self.clean()


            
app = Finder()

            
while(True):
    app.run()