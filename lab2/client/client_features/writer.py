from threading import Thread
from socket import socket 
import time
from file_protocol import FileProtocol

class ClientWriter(Thread):
    def __init__(self, client_socket: socket, protocol : FileProtocol) -> None:
        super().__init__()
        self.client_socket = client_socket
        self.protocol = protocol

    def run(self) -> None:
        self.protocol.send_header(self.client_socket)
        self.protocol.send_data(self.client_socket)
        
        
            