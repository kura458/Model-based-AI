import random
import time

class UserMovementSimulator:

    def __init__(self):
        self.activities = [
            ("stationary",5),
            ("walking",10),
            ("stationary",3),
            ("running",8),
            ("walking",7)
        ]
        self.index = 0
        self.time_in_activity = 0

    def get_movement(self):
        activity, duration = self.activities[self.index]
        self.time_in_activity += 0.1

        if self.time_in_activity >= duration:
            self.index = (self.index + 1) % len(self.activities)
            self.time_in_activity = 0
            activity, duration = self.activities[self.index]

        if activity == "stationary":
            ax = random.gauss(0,0.1)
            ay = random.gauss(0,0.1)
            az = 9.8 + random.gauss(0,0.1)
        else:
            ax = random.uniform(-1,1)
            ay = random.uniform(-1,1)
            az = 9.8 + random.uniform(2,4)

        return {
            "activity": activity,
            "ax": ax,
            "ay": ay,
            "az": az,
            "time": time.time()
        }