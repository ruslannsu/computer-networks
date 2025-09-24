from socket import *
from server_features.server_threads import ServerThread

class Server:
    def __init__(self):
        self.address = ('127.0.0.1', 9000)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(self.address)
        self.server_threads = []
        
        
    def _listen(self):
        self.server_socket.listen()
        while True: 
            client_socket, _  = self.server_socket.accept()
            server_thread = ServerThread(client_socket)
            self.server_threads.append(server_thread)
            server_thread.start()


            

            
            


