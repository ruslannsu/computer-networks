from socket import *

from 



class Server:
    def __init__(self):
        self.address = ('localhost', 5090)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_threads = []
        
        
    def _listen(self):
        self.server_socket.listen()
        while True: 
            client_socket  = self.server_socket.accept()
            self.server_threads.append()
            
            


