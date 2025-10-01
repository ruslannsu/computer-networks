from threading import Thread
import time


class Monitor(Thread):
    def __init__(self, speeds : dict):
        super().__init__()
        self.speeds = speeds

    def run(self):
        while True:
            time.sleep(5)
            for key, val in self.speeds.items():
                print(key)
                print(val)
        