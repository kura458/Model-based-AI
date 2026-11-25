# Smartwatch Step Counter — Model-Based AI Agent

A Python simulation of a smartwatch step counter. The project demonstrates how a model-based agent can use simulated motion readings and an internal stride-length model to estimate steps and walking distance, then refine its estimate through simulated GPS calibration.

## What it demonstrates

- Simulated accelerometer readings and movement detection
- Step counting from movement patterns
- Distance estimation using a learned stride length
- Simulated GPS calibration to adjust stride estimates
- Walking and running activity scenarios
- Activity history and graph visualizations

## AI agent concept

This project illustrates a **model-based agent**: it maintains an internal representation of the user's movement and stride behavior, then updates its estimates as new simulated sensor information becomes available.

## Distance estimation

The basic distance calculation is:

`Distance = Steps × Estimated Stride Length`

For example, 1,000 steps with an estimated stride length of 0.78 metres gives an estimated distance of 780 metres.

## Technology

- Python
- NumPy
- Matplotlib

## Project modules

The project is organized around components for:

- Motion sensor simulation
- Stride-length modeling
- Smartwatch agent behavior
- User movement simulation
- Simulation execution and visualization

Check the current source tree for the exact module paths.

## Run locally

1. Clone the repository:

```bash
git clone https://github.com/kura458/Model-based-AI.git
cd Model-based-AI
```

2. Create and activate a virtual environment (Windows):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the simulation from the directory containing the entry-point script:

```bash
python main.py
```

If the entry point or dependency file has a different name in the current version, follow the repository's source tree.

## Learning outcomes

- Model-based agent architecture
- Sensor and environment simulation
- State updates and estimation
- Distance prediction and calibration
- Data visualization with Matplotlib

## Future directions

Possible extensions include real sensor input, improved activity classification, mobile visualization, and integration with actual GPS data.

---
Academic learning project by [Kura Lemma](https://github.com/kura458).
