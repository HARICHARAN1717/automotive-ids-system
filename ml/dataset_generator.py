import pandas as pd
import random

data = []

# Normal traffic

for _ in range(1000):
	can_id = random.choice([0x100, 0x200, 0x300])
	freq = random.uniform(1, 5)      # normal frequency
	interval = random.uniform(0.5, 2.0)
	data.append([can_id, freq, interval, 0])

# Attack traffic (DoS / Flood)

for _ in range(300):
	can_id = random.choice([0x999, 0xABC])
	freq = random.uniform(10, 50)    # high frequency
	interval = random.uniform(0.01, 0.1)
	data.append([can_id, freq, interval, 1])

df = pd.DataFrame(data, columns=["can_id", "frequency", "interval", "label"])
df.to_csv("ml/can_dataset.csv", index=False)

print("✅ Smart dataset generated!")

