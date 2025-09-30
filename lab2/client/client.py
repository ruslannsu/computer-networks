from socket import *
from client_features.writer import ClientWriter
import yaml


class Client:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.config = self._load_config()
        self.server_address = (self.config['server']['server_ip'], self.config['server']['server_port'])


    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 
        

    def run_client(self):
        self.socket.connect(self.server_address)
        self.client_writer = ClientWriter(self.socket)
        self.client_writer.run()

        


        

