from threading import Thread
from socket import socket

class ServerThread(Thread):
    def __init__(self, client_socket: socket) -> None:
        self.client_socket = client_socket


    def run(self) -> None:
        while (True):
            buffer = self.client_socket.recv(1024)
            print(buffer)









        

        

            
        