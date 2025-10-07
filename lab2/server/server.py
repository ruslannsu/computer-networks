from socket import *
from server_features.server_threads import ServerThread
import yaml
from server_features.server_reader import ServerReader
from server_features.monitor import Monitor
import logging





class Server:
    def __init__(self):
        self.address = ('127.0.0.1', 9000)
    
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server_socket.bind(self.address)
        self.server_threads = []
        self.speeds = {}
        self.server_reader = ServerReader(5, 'MAGIC', 13, 5, 10000000000000, 4096, self.speeds)
        self.monitor = Monitor(speeds=self.speeds)
        self._init_logging()


    def _init_logging(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f"{__name__}.log", mode='w')
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)


    def __exit__(self):
        self.server_socket.close()


    def _load_config(self):
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f) 
        
    def _listen(self):
        self.monitor.start()
        self.server_socket.listen()
        while True: 
            client_socket, _  = self.server_socket.accept()
            server_thread = ServerThread(client_socket, self.server_reader)
            self.server_threads.append(server_thread)
            server_thread.start()


            

            
            


