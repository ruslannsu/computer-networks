from threading import Thread
from socket import socket
import time

class ServerThread(Thread):
    def __init__(self, client_socket: socket) -> None:
        super().__init__()
        self.client_socket = client_socket

    def run(self) -> None:
        while (True):
            buffer = self.client_socket.recv(10)
            print(len(buffer))
            print(buffer.decode('utf-8'))
            print(len(buffer.decode('utf-8')))
            time.sleep(10)










        

        

            
        