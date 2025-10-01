import socket
import time

class ServerReader():
    def __init__(self, magic_len: int, magic_word : str,file_total_size_len: int, file_header_size_len: int, total_size_max : int, header_max_size : int) -> None:
        self.file_tota_size_len = file_total_size_len
        self.file_header_size_len = file_header_size_len
        self.magic_len = magic_len
        self.magic_word = magic_word
        self.header = None
        self.code = 'utf-8'
        self.total_max_size = total_size_max
        self.hedaer_max_size = header_max_size
        

    def read_exactly(self, size : int, sock : socket):
        data = b''
        while len(data) < size:
            chunk = sock.recv(size - len(data))
            if not chunk:  
                break
            data += chunk
        return data

    def _get_optimal_chunk_size(self, file_size):
        if file_size < 1024 * 1024: 
            return 4096
        elif file_size < 100 * 1024 * 1024:  
            return 65536
        else:  
            return 262144  



    def read_header(self, sock : socket) -> None:
        magic_word = self.read_exactly(self.magic_len, sock)
        print(magic_word)
        if (magic_word.decode(self.code) != self.magic_word):
            raise ConnectionError('NO MAGIC')
        
        self.file_total_size = self.read_exactly(self.file_tota_size_len, sock)
        print(int.from_bytes(self.file_total_size, 'big'))
        if (int.from_bytes(self.file_total_size, 'big') >= self.total_max_size):
            raise ConnectionError('SIZE ERROR')
        self.header_size = int.from_bytes(self.read_exactly(self.file_header_size_len, sock), 'big')
        print(self.header_size)
        if (int.from_bytes(self.file_total_size, 'big') >= self.hedaer_max_size):
            raise ConnectionError('SIZE ERROR')

        self.file_header = self.read_exactly(self.header_size, sock)
        print(self.file_header.decode(self.code))
        self.data_size = (int.from_bytes(self.file_total_size, 'big')) - len(magic_word) - self.header_size - self.file_header_size_len - self.file_tota_size_len

    def read_data(self, sock : socket) -> None:
        size = self._get_optimal_chunk_size(int.from_bytes(self.file_total_size, 'big'))
        self.file = open('./get', 'wb')
        total = 0
        print(f"total size{self.data_size}")
        while (total < self.data_size):
            buffer = self.read_exactly(size, sock)
            print(len(buffer))
            print("-buffer len data")
            total += len(buffer)
            self.file.write(buffer)
            self.file.flush() 
        
            
            








        
        
        




        


        



        
