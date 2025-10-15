from threading import Thread
import time


class Monitor(Thread):
    def __init__(self, speeds : dict) -> None:
        super().__init__()
        self.speeds = speeds
        self.time_window = 2


    def update_speed(self, start_time: int, end_time: int, bytes_num: int, address) -> bool:
        if (end_time - start_time >= 2):
            self.speeds[address] = bytes_num / (end_time - start_time)
            return True
        return False    
            

    def run(self) -> None:
        while True:
            time.sleep(5)
            for key, val in self.speeds.items():
                print(key)
                print(val)
        