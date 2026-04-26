import json
import time
import joblib
import pandas as pd
import random

LOG_FILE = "logs/alerts.log"

# Load ML model
model = joblib.load("ml/ids_model.pkl")

blocked_ids = set()
threat_score = 0


def auto_isolate(can_id):
    print(f"[🚫 ISOLATED ECU] {can_id}")
    blocked_ids.add(can_id)


def log_alert(can_id, attack, severity):
    global threat_score

    # Increase threat score
    if severity == "CRITICAL":
        threat_score += 20
    elif severity == "HIGH":
        threat_score += 10

    if threat_score > 100:
        threat_score = 100

    # Auto isolation logic
    if threat_score >= 50:
        auto_isolate(can_id)

    alert = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "type": attack,
        "can_id": can_id,
        "severity": severity,
        "threat_score": threat_score
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(alert) + "\n")

    print(f"[🚨 {severity}] {attack} → {can_id} | Score: {threat_score}")


def extract_features(can_id):
    freq = random.uniform(1, 50)
    interval = random.uniform(0.01, 2.0)

    return pd.DataFrame([[int(can_id, 16), freq, interval]],
                        columns=["can_id", "frequency", "interval"])


def process_message(can_id):
    if can_id in blocked_ids:
        print(f"[⛔ IGNORED] {can_id}")
        return

    # ML Detection
    features = extract_features(can_id)
    prediction = model.predict(features)[0]

    # Rule-based detection
    attack_type = None
    severity = "HIGH"

    if can_id == "0x999":
        attack_type = "DoS Attack"
        severity = "CRITICAL"

    elif can_id == "0xABC":
        attack_type = "Spoof Attack"

    # Hybrid detection
    if prediction == 1:
        if attack_type:
            log_alert(can_id, attack_type, severity)
        else:
            log_alert(can_id, "ML Detected Attack", "HIGH")

        blocked_ids.add(can_id)
        print(f"[🛡️ BLOCKED] {can_id}")
    else:
        print(f"[✔] Normal: {can_id}")
