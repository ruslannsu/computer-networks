from socket import *
from server_features.server_threads import ServerThread
import yaml
from server_features.server_reader import ServerReader



class Server:
    def __init__(self):
        self.address = ('127.0.0.1', 9000)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(self.address)
        self.server_threads = []
        self.server_reader = ServerReader(5, 'MAGIC', 13, 5, 1000000000, 4096)


    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 
        
        
    def _listen(self):
        self.server_socket.listen()
        while True: 
            client_socket, _  = self.server_socket.accept()
            server_thread = ServerThread(client_socket, self.server_reader)
            self.server_threads.append(server_thread)
            server_thread.start()


            

            
            


