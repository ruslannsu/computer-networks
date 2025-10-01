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
        self.reader.run_server_reader(self.client_socket)
        
        
        










        

        

            
        