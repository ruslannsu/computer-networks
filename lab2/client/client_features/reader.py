from threading import Thread



class Reader():
    def __init__(self, socket):
        self.socket = socket
        self.read_thread = Thread()


    def _read(self):
        while True: 
            

