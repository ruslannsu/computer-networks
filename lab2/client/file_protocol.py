import os
import socket

class FileProtocol():
    def __init__(self, file_path: str, file_name : str, file_header_size : int) -> None:
        self.file_path = file_path
        self.enc = 'utf-8'
        self.file = open(self.file_path, mode='b')
        self.file_size = int.to_bytes(os.stat(self.file_path).st_size, byteorder='big')
        self.file_name = file_name.encode(self.enc)
        self.file_header_size = int.to_bytes(file_header_size, byteorder='big')
        self.magic_word = 'MAGIC'.encode(self.enc)


    def send_header(self, sock : socket) -> None:
        sock.send(self.magic_word)
        sock.send(self.file_size)
        sock.send(self.file_header_size)
        sock.send(self.file_name)


        
        

         

        
        
    
         

