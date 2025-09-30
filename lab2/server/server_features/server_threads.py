from threading import Thread
from socket import socket
import time

class ServerThread(Thread):
    def __init__(self, client_socket: socket) -> None:
        super().__init__()
        self.client_socket = client_socket

    def run(self) -> None:
        while (True):
            buffer = self.client_socket.recv(5)
            print(buffer.decode('utf-8'))
            buffer = self.client_socket.recv(13)
            print(int.from_bytes(buffer, 'big'))
            break

            time.sleep(10)










        

        

            
        