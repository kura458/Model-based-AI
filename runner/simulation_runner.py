import time
import random
import matplotlib.pyplot as plt

from agents.smartwatch_agent import SmartwatchAgent
from simulators.user_movement import UserMovementSimulator


class SimulationRunner:

    def __init__(self):
        self.agent = SmartwatchAgent()
        self.user = UserMovementSimulator()

    def run(self, duration=60):
        print("\n⌚ Smartwatch Step Counter Simulation\n")

        start = time.time()
        last_gps = start
        last_steps = 0

        while time.time() - start < duration:
            movement = self.user.get_movement()
            self.agent.run_step(movement)

            current = time.time()

            # GPS calibration every 15 seconds
            if current - last_gps >= 15:
                steps = self.agent.steps - last_steps
                actual_stride = 0.78 + random.gauss(0, 0.05)
                gps_distance = steps * actual_stride

                print(f"\n📍 GPS Fix: {gps_distance:.1f} m")

                self.agent.model.calibrate_with_gps(
                    gps_distance,
                    steps
                )

                last_gps = current
                last_steps = self.agent.steps

            time.sleep(0.1)

        print("\n\nSimulation Finished\n")

        # 👉 THIS CALLS THE GRAPH
        self.visualize()

    # ✅ THIS FUNCTION WAS MISSING (VERY IMPORTANT)
    def visualize(self):
        times = [h["time"] for h in self.agent.history]
        steps = [h["steps"] for h in self.agent.history]
        distance = [h["distance"] for h in self.agent.history]

        # -------- GRAPH 1: STEPS --------
        plt.figure()
        plt.plot(times, steps)
        plt.title("Steps Over Time")
        plt.xlabel("Time")
        plt.ylabel("Steps")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # -------- GRAPH 2: DISTANCE --------
        plt.figure()
        plt.plot(times, distance)
        plt.title("Distance Over Time")
        plt.xlabel("Time")
        plt.ylabel("Meters")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Optional summary
        print("\nTotal Steps:", steps[-1])
        print("Total Distance:", round(distance[-1], 2), "meters")
        print("Model Confidence:", self.agent.model.confidence)