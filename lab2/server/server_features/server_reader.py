import socket
import time
import logging



class ServerReader():
    def __init__(self, magic_len: int, magic_word : str,file_total_size_len: int, file_header_size_len: int, total_size_max : int, header_max_size : int, speeds : dict) -> None:
        self.file_tota_size_len = file_total_size_len
        self.file_header_size_len = file_header_size_len
        self.magic_len = magic_len
        self.magic_word = magic_word
        self.header = None
        self.code = 'utf-8'
        self.total_max_size = total_size_max
        self.hedaer_max_size = header_max_size
        self.speeds = speeds
        self.logger = self._get_logger()

        
        


    def _get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(f"{__name__}.log", mode='w')
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger


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


    def _is_correct(self) -> bool:
        if (int.from_bytes(self.file_total_size, 'big') != self.readed_size + len(self.magic_word) + self.header_size + self.file_header_size_len + self.file_tota_size_len):
            return False
        return True 

    def read_header(self, sock : socket) -> None:
        magic_word = self.read_exactly(self.magic_len, sock)
        print(magic_word)
        if (magic_word.decode(self.code) != self.magic_word):
            raise ConnectionError('NO MAGIC')
        
        self.file_total_size = self.read_exactly(self.file_tota_size_len, sock)
        print(int.from_bytes(self.file_total_size, 'big'))
        if (int.from_bytes(self.file_total_size, 'big') >= self.total_max_size):
            raise ConnectionError('SIZE TOTAL ERROR')
        self.header_size = int.from_bytes(self.read_exactly(self.file_header_size_len, sock), 'big')
        print(self.header_size)
        if (self.header_size >= self.hedaer_max_size):
            raise ConnectionError('SIZE ERROR')

        self.file_header = self.read_exactly(self.header_size, sock)
        print(self.file_header.decode(self.code))
        self.data_size = (int.from_bytes(self.file_total_size, 'big')) - len(magic_word) - self.header_size - self.file_header_size_len - self.file_tota_size_len
        
        self.logger.info(f"GET FILE HEADER: {self.file_header.decode(self.code)}")



    def read_data(self, sock : socket, start_time_session : int) -> None:
        size = self.data_size

        self.file = open(f'./{self.file_header.decode(self.code)}', 'wb')
        total = 0
        print(f"data size{self.data_size}")
        while (total < self.data_size):
            start_time = time.time()
            buffer = sock.recv(1024)
            print(len(buffer))
            print("-buffer len data")
            total += len(buffer)
            self.file.write(buffer)
            self.file.flush()
            end_time = time.time()
            if (int(end_time) - int(start_time_session)) > 0:
                if (((int(end_time) - int(start_time)) == 0)):
                    speed, mid_speed = (len(buffer), total / int(end_time - start_time_session))
                    address, _  = sock.getpeername()
                    self.speeds[address] = (speed, mid_speed)

                else:
                    speed, mid_speed  = (len(buffer) / (int(end_time) - int(start_time)), total / int(end_time - start_time_session))
                    address, _ = sock.getpeername()
                    self.speeds[address] = (speed, mid_speed)
            
        self.readed_size = total

        self.logger.info(f"GET FILE DATA WITH SIZE {total}")

    

    def run_server_reader(self, sock : socket):
        start_time = time.time()
        self.read_header(sock)
        self.read_data(sock, start_time)
        if self._is_correct():
            sock.send('FILE ACCEPTED'.encode(self.code))
            
        else:
            sock.sendall('SOMETHING WRONG WITH FILE SIZE'.encode(self.code))
        
        
        








        
        
        




        


        



        
