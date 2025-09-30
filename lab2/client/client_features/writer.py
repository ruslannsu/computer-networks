from threading import Thread
from socket import socket 
import time

class ClientWriter(Thread):
    def __init__(self, client_socket: socket) -> None:
        super().__init__()
        self.client_socket = client_socket

    def run(self) -> None:
        while True:
            string = "Hello world"
            buffer = string.encode('utf-8') 
            self.client_socket.send(buffer)
            time.sleep(10)
            