import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from predictor import load_model_and_predict

def predict():
    try:
        type_mapping = {"L": 0, "M": 1, "H": 2}
        machine_type = type_mapping[type_var.get()]
        features = [
            machine_type,
            float(entry_temp.get()),
            float(entry_process.get()),
            float(entry_speed.get()),
            float(entry_torque.get()),
            float(entry_wear.get())
        ]
        result = load_model_and_predict(np.array([features]))
        messagebox.showinfo("Prediction Result", f"Prediction: {result[0]}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or model error:\n{str(e)}")

root = tk.Tk()
root.title("Predictive Maintenance GUI")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Machine Type").pack()
type_var = ttk.Combobox(root, values=["L", "M", "H"])
type_var.set("L")
type_var.pack()

tk.Label(root, text="Air Temperature").pack()
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Label(root, text="Process Temperature (K)").pack()
entry_process = tk.Entry(root)
entry_process.pack()

tk.Label(root, text="Rotational Speed [rpm]").pack()
entry_speed = tk.Entry(root)
entry_speed.pack()

tk.Label(root, text="Torque [Nm]").pack()
entry_torque = tk.Entry(root)
entry_torque.pack()

tk.Label(root, text="Tool Wear [min]").pack()
entry_wear = tk.Entry(root)
entry_wear.pack()

tk.Button(root, text="Predict", command=predict).pack(pady=10)

root.mainloop()
