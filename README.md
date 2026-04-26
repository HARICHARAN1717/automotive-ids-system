# 🚗 Automotive Intrusion Detection & Response System

##  Overview

This project is a real-time Intrusion Detection and Response System (IDRS) for automotive CAN bus networks.

It combines:

* Rule-based attack detection
* Machine Learning-based anomaly detection
* Real-time visualization dashboard
* Automated ECU isolation

---

## Features

*  Detects DoS, Spoof, and ML-based anomalies
*  Dynamic threat scoring (0–100)
*  Automatic ECU isolation
*  Live dashboard with attack statistics
*  Attack timeline visualization

---

##  Tech Stack

* Python
* Flask + Socket.IO
* Scikit-learn (Random Forest)
* Chart.js (Frontend visualization)

---

##  How to Run

### 1. Setup environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Start dashboard

```bash
python3 dashboard/app.py
```

### 3. Run simulator

```bash
python3 simulator/simulator.py
```

---

##  Demo

(Add screenshots here)

---

##  Future Improvements

* Real CAN hardware integration
* Advanced anomaly detection models
* ECU-level behavioral profiling

---

##  Author

Haricharan
