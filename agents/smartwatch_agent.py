from datetime import datetime
from sensors.motion_sensor import MotionSensor
from models.stride_model import StrideModel

class SmartwatchAgent:

    def __init__(self):
        self.sensor = MotionSensor()
        self.model = StrideModel()
        self.steps = 0
        self.distance = 0
        self.activity = "stationary"
        self.history = []

    def perceive(self, movement):
        reading = self.sensor.read(
            movement["ax"],
            movement["ay"],
            movement["az"]
        )

        if self.sensor.detect_step(reading):
            self.steps += 1

        self.activity = movement["activity"]

    def decide(self):
        prediction = self.model.predict_distance(
            self.steps,
            self.activity
        )
        self.distance = prediction["distance"]
        return prediction

    def act(self, prediction):
        if prediction["confidence"] > 0.8:
            msg = f"📊 {self.steps} steps | {self.distance:.1f} m"
        elif prediction["confidence"] > 0.5:
            msg = f"📈 Estimating {self.distance:.1f} m"
        else:
            msg = f"⚠️ Low confidence {self.distance:.1f} m"

        print("\r" + msg, end="")

    def update_history(self):
        self.history.append({
            "time": datetime.now(),
            "steps": self.steps,
            "distance": self.distance
        })

    def run_step(self, movement):
        self.perceive(movement)
        prediction = self.decide()
        self.act(prediction)
        self.update_history()