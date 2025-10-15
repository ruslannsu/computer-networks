import os
import socket
import time
class FileProtocol():
    def __init__(self, file_path: str, file_header_size_len : int, file_data_size_len : int) -> None:
        self.file_path = file_path
        self.enc = 'utf-8'
        self.file = open(self.file_path, mode='rb')
        self.data_size = os.stat(self.file_path).st_size
        self.data_size_coded = os.stat(self.file_path).st_size.to_bytes(file_data_size_len, 'big')
        print("FILE NAME:")
        self.file_name = file_path.encode(self.enc)
        print(self.file_name)
        self.file_header_size = len(file_path).to_bytes(file_header_size_len, byteorder='big')
        self.magic_word = 'MAGIC'.encode(self.enc)
        self.file_total_size = len(file_path) + file_header_size_len + len(self.magic_word) + self.data_size + file_data_size_len
        self.file_total_size = self.file_total_size.to_bytes(file_data_size_len, 'big')

        
    def send_header(self, sock : socket) -> None:
        sock.send(self.magic_word)
        sock.send(self.file_total_size)
        sock.send(self.file_header_size)
        sock.send(self.file_name)
    

    def _get_optimal_chunk_size(self, file_size):
        if file_size < 1024 * 1024: 
            return 4096
        elif file_size < 100 * 1024 * 1024:  
            return 65536
        else:  
            return 262144  

    def send_data(self, sock : socket) -> None:
        size = self._get_optimal_chunk_size(self.data_size)
        sended = 0
        while (sended < self.data_size):
            buffer = self.file.read(size)
            print(len(buffer))
            time.sleep(2)
            sended += len(buffer)
            sock.sendall(buffer)

         

        
        
    
         

