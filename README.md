Smartwatch Step Counter AI Agent
A Model-Based AI Agent simulation that mimics the behavior of a smartwatch fitness tracker.
The system detects movement, counts steps, estimates traveled distance, and improves accuracy using simulated GPS calibration.

📌 Project Overview
This project demonstrates how an intelligent wearable system can:
Detect user movement using simulated motion sensors
Count steps automatically
Estimate walking/running distance
Learn user stride length over time
Visualize activity using graphs
The simulation is inspired by real-world smartwatch devices such as:
Apple Watch
Samsung Galaxy Watch
Fitbit Charge
🧠 AI Agent Type
This project implements a Model-Based AI Agent because it:
Maintains an internal state
Learns stride behavior using GPS calibration
Uses previous data to improve future predictions
Continuously updates decisions based on sensor input
⚙️ Features
✅ Motion sensing using accelerometer simulation
✅ Automatic step detection
✅ Distance estimation using stride length
✅ GPS-based stride calibration
✅ Walking and running activity simulation
✅ Real-time console output
✅ Data visualization using graphs
✅ Activity history tracking
🏗️ Project Structure
smartwatch_simulation/
│├── main.py
├── requirements.txt
│├── models/│   
    └── stride_model.py
    │├── sensors/
    │   └── motion_sensor.py
    │├── simulators/
    │   └── user_movement.py
│├── agents/
    │   └── smartwatch_agent.py
    │└── runner/    
    └── simulation_runner.py

📡 PEAS Description
ComponentDescriptionPerformance MeasureAccurate step counting and distance estimationEnvironmentUser movement (walking, running, stationary)ActuatorsConsole display outputSensorsSimulated accelerometer motion sensor
🔄 System Workflow
User Movement 
↓Motion Sensor Reads Acceleration      
↓Step Detection      
↓Distance Estimation     
↓GPS Calibration      
↓Display Output      
↓Graph Visualization

📐 Distance Formula
The system estimates distance using:
Distance = Steps × Stride Length
Example:
1000 steps × 0.78 m = 780 meters
🛠️ Technologies Used
Python
NumPy
Matplotlib
🚀 Installation & Setup
1️⃣ Clone Repository
git clone <your-repository-url>cd smartwatch_simulation

2️⃣ Create Virtual Environment
Windows
python -m venv venv
Activate:
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

▶️ Run the Project
python main.py

📊 Expected Output
⌚ Smartwatch Step Counter Simulation⚠️ Low confidence 78.0 m📍 GPS Fix: 83.9 m📡 GPS calibration -> stride 0.84 m📈 Estimating 183.8 mSimulation Finished
The simulation also generates:
Steps over time graph
Distance over time graph
📈 Visualization
The project visualizes:
Step count progression
Distance estimation progression
using Matplotlib.
🧩 Main Modules
MotionSensor
Simulates accelerometer readings and detects movement.
StrideModel
Predicts distance and learns user stride behavior.
SmartwatchAgent
Main AI agent that performs perception, decision making, and actions.
UserMovementSimulator
Simulates different user activities.
SimulationRunner
Controls the simulation loop and visualization.
🎯 Learning Outcomes
This project demonstrates:
AI agent architecture
Model-based decision making
Sensor simulation
Distance prediction
GPS calibration
Real-time system simulation
Data visualization
📌 Future Improvements
Real smartwatch sensor integration
Machine learning-based activity recognition
Mobile application interface
Heart rate monitoring
Real GPS integration
