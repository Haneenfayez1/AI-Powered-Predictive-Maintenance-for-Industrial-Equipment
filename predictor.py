import numpy as np
from keras.models import load_model

model = load_model("lstm_model.keras")

def load_model_and_predict(input_array):
    input_array = input_array.reshape((input_array.shape[0], 1, input_array.shape[1]))
    prediction = model.predict(input_array)
    return ["Failure" if p[0] > 0.5 else "Normal" for p in prediction] 