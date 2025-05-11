
# retraining.py
import pandas as pd
import numpy as np
import tensorflow as tf
import mlflow
import mlflow.tensorflow

# Load data
data = pd.read_csv("sensors_data.csv")
X = data[['Rotational_speed', 'Torque', 'Tool_wear', 'Vibration', 'Process_temperature']].values
X = X.reshape((X.shape[0], 1, X.shape[1]))
y = np.random.rand(len(X))  # Simulated targets

# Define simple LSTM model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(64, input_shape=(1, 5)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')

# Track with MLflow
mlflow.tensorflow.autolog()
with mlflow.start_run():
    model.fit(X, y, epochs=3, batch_size=16)
    model.save("lstm_model.keras")
