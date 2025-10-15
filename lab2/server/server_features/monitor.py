from threading import Thread
import time

class Monitor(Thread):
    def __init__(self, speeds : dict) -> None:
        super().__init__()
        self.speeds = speeds
        self.time_window = 1

    def update_speed(self, start_time: int, end_time: int, bytes_num: int, address, session_start_time: int, total: int) -> bool:
        if (end_time - start_time >= self.time_window):
            self.speeds[address] = ((bytes_num / (end_time - start_time)), total / (time.time() - session_start_time) ,time.time())
            return True
        return False

    def run(self) -> None:
        while True:
            time.sleep(3)
            act_time = time.time()
            for key, val in self.speeds.items():
                if (val[1] - act_time >= 3):
                    self.speeds.pop(key)

                print(key)
                print("SPEED:", val[0])
                print("SESSION SPEED:", val[1])



        