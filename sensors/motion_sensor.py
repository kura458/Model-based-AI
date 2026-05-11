import random
import numpy as np
import time

class MotionSensor:

    def __init__(self):
        self.noise = 0.05
        self.step_threshold = 1.2

    def read(self, ax, ay, az):
        x = ax + random.gauss(0, self.noise)
        y = ay + random.gauss(0, self.noise)
        z = az + random.gauss(0, self.noise)

        magnitude = np.sqrt(x*x + y*y + z*z)

        return {
            "x": x,
            "y": y,
            "z": z,
            "magnitude": magnitude,
            "time": time.time()
        }

    def detect_step(self, reading):
        return reading["magnitude"] > (9.8 + self.step_threshold)