from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained ML model
model_path = os.path.join("models", "crop_model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from form
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
    except ValueError:
        return "Invalid input! Please enter numeric values."

    # Prepare input for model
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    
    # Predict crop
    predicted_crop = model.predict(features)[0]
    
    return render_template('result.html', crop=predicted_crop)

if __name__ == "__main__":
    app.run(debug=True)
