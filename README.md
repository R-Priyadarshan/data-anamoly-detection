# Project 1 — IoT Device Data Anomaly Detection (Simulated)

## Overview
Simulates IoT devices posting sensor readings to a simple Flask server. Trains an Isolation Forest to detect anomalies and produces a scatter plot of anomalies.

## Setup
```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run
1. Start server: `python server.py`
2. In another terminal run simulator: `python device_simulator.py`
3. After some data is collected, train: `python train_model.py`
4. Detect & plot: `python detect_live.py`
