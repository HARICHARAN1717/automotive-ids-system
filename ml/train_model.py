import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("ml/can_dataset.csv")

X = df[["can_id", "frequency", "interval"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml/ids_model.pkl")

print("✅ Smart ML model trained!")

