from threading import Thread
from socket import socket
import time
from server_features.server_reader import ServerReader

class ServerThread(Thread):
    def __init__(self, client_socket: socket, reader : ServerReader) -> None:
        super().__init__()
        self.client_socket = client_socket
        self.reader = reader

    def run(self) -> None:
        self.reader.read_header(self.client_socket)
        self.reader.read_data(self.client_socket)
        










        

        

            
        