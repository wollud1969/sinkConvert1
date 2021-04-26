import threading
import time


class Tick(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.condition = threading.Condition()
        self.interval = interval
    
    def waitForTick(self):
        with self.condition:
            self.condition.wait()
    
    def run(self):
        while True:
            with self.condition:
                self.condition.notify()
            time.sleep(self.interval)