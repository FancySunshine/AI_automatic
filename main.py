import time
import numpy as np
import threading


class MainAutoMatic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.linear = np.random.randint(1000, 15000)
        self.outline = np.random.randint(1000, 15000)

    def led_right(self):
        while True:
            time.sleep(1)
            if self.linear >= self.outline:
                SunAutoMatic().run()
            else:
                SunAutoMatic().run()


class LedAutoMatic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.led = np.random.randint(100, 10000)

    def run(self):
        while True:
            time.sleep(1)
            if self.led == 100 and 10000:
                print("LED 키자")
            else:
                print("LED 끄자")


class SunAutoMatic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.linear = np.random.randint(1000, 15000)
        self.outline = np.random.randint(1000, 15000)

    def run(self):
        while True:
            time.sleep(1)
            if self.linear < self.outline:
                print("커텐 치자")
                LedAutoMatic().run()
            else:
                print("커텐 닫자")
                LedAutoMatic().run()


if __name__ == "__main__":
    MainAutoMatic().led_right()
