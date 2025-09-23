import struct
import time 
from socket import *
import yaml

class Finder(object):
    def __init__(self):
        self.config = self._load_config()
        self._init_properties()
        self._init_sockets()        

    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 

    def _init_properties(self):
        self.multicast_group = (self.config['multicast']['group'], self.config['multicast']['port'])
        self.message = self.config['multicast']['message']
        self.enc = self.config['multicast']['encoding']
        self.time_offset = self.config['time']['offset']
        self.buffer_size = self.config['network']['buffer_size']
        self.dict = {}

    def _init_sockets(self):
        self.rec_socket = self._create_receive_socket()
        self.send_socket = self._create_send_socket()
    
    def _create_receive_socket(self):
        rec_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        rec_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        rec_socket.bind(('', self.multicast_group[1]))
        mreq = struct.pack("4s4s", inet_aton(self.multicast_group[0]), inet_aton('0.0.0.0'))
        rec_socket.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)
        return rec_socket
        
    def _create_send_socket(self):
        send_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        send_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        send_socket.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, 2)
        return send_socket

    def _clean(self):
        time_ = int(time.time())
        for key, value in list(self.dict.items()):
            if (time_ - value > self.time_offset):
                self.dict.pop(key)
                print(f"DIED: {key}")
                self._screen()   

    def _screen(self):
        print('ALIVE: ')
        for key, _ in self.dict.items():
            print(key)    
        print('')   
   

    def run(self):
        while (True):
            send_message = self.message.encode(self.enc)
            self.send_socket.sendto(send_message, self.multicast_group)
            message, address = self.rec_socket.recvfrom(self.buffer_size)
            message = message.decode(self.enc)
            if (message != self.message ):
                continue
            if (not(address in self.dict)):
                print(f"NEW: {address}")
                self.dict[address] = time.time()
                self._screen()
            else:
                self.dict[address] = time.time()
            self._clean()
    


