import numpy as np

class StrideModel:

    def __init__(self):
        self.base_stride_length = 0.78
        self.confidence = 0.5
        self.stride_history = []

    def calibrate_with_gps(self, gps_distance, steps):
        if steps <= 0:
            return
        stride = gps_distance / steps
        self.stride_history.append(stride)

        if len(self.stride_history) > 10:
            self.stride_history.pop(0)

        self.base_stride_length = np.mean(self.stride_history)
        self.confidence = min(0.95, 0.5 + len(self.stride_history) * 0.05)

        print(f"\n📡 GPS calibration -> stride {stride:.2f} m")

    def predict_distance(self, steps, activity):
        stride = self.base_stride_length * self.activity_adjustment(activity)
        distance = steps * stride
        uncertainty = (1 - self.confidence) * distance * 0.2

        return {
            "distance": distance,
            "stride": stride,
            "confidence": self.confidence,
            "uncertainty": uncertainty
        }

    def activity_adjustment(self, activity):
        factors = {
            "walking": 1.0,
            "running": 1.3,
            "jogging": 1.15,
            "stairs": 0.6,
            "stationary": 0.0
        }
        return factors.get(activity, 1.0)