import numpy as np
import joblib
from skopt import gp_minimize
from skopt.space import Real
from skopt.utils import use_named_args

model_d = joblib.load("models/droplet_diameter_model.pkl")
model_r = joblib.load("models/droplet_rate_model.pkl")

space = [
    Real(0.5, 5.0, name='Flow rate ratio'),
    Real(0.01, 2.0, name='Capillary number'),
    Real(100, 500, name='Dispersed flow rate ul/h'),
]


fixed = {
    "Orifice width (um)": 22.5,
    "Normalized channel depth": 1.0,
    "Normalized continuous inlet": 1.0,
    "Normalized dispersed inlet": 1.0,
    "Normalized outlet width": 1.0,
    "viscosity ratio": 1.6
}

# Target values
target_diameter = 30.0
target_rate = 5000.0

@use_named_args(space)
def objective(**params):
    X = [
        fixed["Orifice width (um)"],
        fixed["Normalized channel depth"],
        params["Flow rate ratio"],
        params["Capillary number"],
        fixed["Normalized continuous inlet"],
        fixed["Normalized dispersed inlet"],
        fixed["Normalized outlet width"],
        fixed["viscosity ratio"],
        params["Dispersed flow rate ul/h"]
    ]
    pred_d = model_d.predict([X])[0]
    pred_r = model_r.predict([X])[0]
    return (pred_d - target_diameter)**2 + 0.0001 * (pred_r - target_rate)**2

res = gp_minimize(objective, space, n_calls=30, random_state=42)


print("\n Best Parameters Found:")
for name, val in zip(["Flow rate ratio", "Capillary number", "Dispersed flow rate ul/h"], res.x):
    print(f"{name}: {val:.4f}")
