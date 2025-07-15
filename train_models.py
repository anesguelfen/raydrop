import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import os

df = pd.read_excel("data/raw_data.xlsx", sheet_name="Fig 1 & 2")
df = df.dropna(subset=["Observed droplet diameter (um)", "Observed generation rate (Hz)"])

X = df[[
    "Orifice width (um)",
    "Normalized channel depth",
    "Flow rate ratio",
    "Capillary number",
    "Normalized continuous inlet",
    "Normalized dispersed inlet",
    "Normalized outlet width",
    "viscosity ratio",
    "Dispersed flow rate ul/h"
]]

y_d = df["Observed droplet diameter (um)"]
y_r = df["Observed generation rate (Hz)"]

X_train, X_test, y_d_train, y_d_test, y_r_train, y_r_test = train_test_split(
    X, y_d, y_r, test_size=0.2, random_state=42)

model_d = GradientBoostingRegressor().fit(X_train, y_d_train)
model_r = GradientBoostingRegressor().fit(X_train, y_r_train)

os.makedirs("models", exist_ok=True)
joblib.dump(model_d, "models/droplet_diameter_model.pkl")
joblib.dump(model_r, "models/droplet_rate_model.pkl")

print("Models trained and saved.")
