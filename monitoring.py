
# monitoring.py
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_squared_error

# Load model and new data
model = tf.keras.models.load_model("lstm_model.keras")
data = pd.read_csv("sensors_data.csv")

# Simulate real-time monitoring
errors = []
for i in range(len(data) - 1):
    input_data = data.iloc[i][['Rotational_speed', 'Torque', 'Tool_wear', 'Vibration', 'Process_temperature']].values
    input_data = np.array(input_data).reshape((1, 1, 5))
    pred = model.predict(input_data)
    actual = 0  # Simulated value, replace with real label if available
    error = mean_squared_error([actual], [pred[0][0]])
    errors.append(error)

print("Average prediction error:", np.mean(errors))
