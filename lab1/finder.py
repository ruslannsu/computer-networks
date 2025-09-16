import struct
import time 
from socket import *
import yaml




class Finder(object):
    def __init__(self):

        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)

        self.multicast_group = (config['multicast']['group'], config['multicast']['port'])
        self.message = config['multicast']['message']
        self.enc = config['multicast']['encoding']
        self.time_offset = config['time']['offset']
        self.buffer_size = config['network']['buffer_size']
        self.send_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.send_socket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
        self.rec_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.rec_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.rec_socket.bind(('', self.multicast_group[1]))
        mreq = struct.pack("4s4s", inet_aton(self.multicast_group[0]), inet_aton('0.0.0.0'))
        self.rec_socket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
        self.dict = {}
        
    def clean(self):
        time_ = int(time.time())
        for key, value in list(self.dict.items()):
            if (time_ - value > self.time_offset):
                self.dict.pop(key)
                print(f"{key} died")
                self.screen()

    def screen(self):
        print('alive')
        for key, _ in self.dict.items():
            print(key)    

    def run(self):
        while (True):
            send_message = self.message.encode(self.enc)
            self.send_socket.sendto(send_message, self.multicast_group)
            message, address = self.rec_socket.recvfrom(self.buffer_size)
            message = message.decode(self.enc)
            if (message != self.message):
                continue
            if (not(address in self.dict)):
                print(f"new: {address}")
                self.screen()
                
            self.dict[address] = time.time()
            self.clean()
            


            
app = Finder()

            
while(True):
    app.run()