from socket import *
from client_features.writer import ClientWriter
from client_features.reader import ClientReader
from file_protocol import FileProtocol
import yaml


class Client:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.config = self._load_config()
        self.socket.bind((self.config['client']['ip'], self.config['client']['port']))
        self.config = self._load_config()
        self.server_address = (self.config['server']['server_ip'], self.config['server']['server_port'])
        self.file_path = self.config['file']['file_path']
        self.protocol = FileProtocol('f1', 5, 13)
      
    

    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 
        

    def run_client(self):
        self.socket.connect(self.server_address)
        self.client_writer = ClientWriter(self.socket, self.protocol)
        self.client_writer.start()
        self.client_reader = ClientReader(self.socket)
        self.client_reader.start()
        

        


        

