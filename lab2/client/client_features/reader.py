from threading import Thread
from socket import socket 

import time
class ClientReader(Thread):
    def __init__(self, socket : socket):
        super().__init__()
        self.socket = socket
        self.read_thread = Thread()


    def _read(self):
        while True: 
            buffer = self.socket.recv(1024)
            if (len(buffer) != 0):
                print(buffer.decode('utf-8'))
            time.sleep(5)
    

    def run(self):
        self._read()

            

