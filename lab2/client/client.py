from socket import *
from client_features.writer import ClientWriter

class Client:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)

    def run_client(self):
        self.socket.connect(('127.0.0.1', 9000))
        self.client_writer = ClientWriter(self.socket)

        


        

