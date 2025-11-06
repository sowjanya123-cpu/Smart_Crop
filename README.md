# 🌾 Smart Crop Recommendation System

A web-based application built using **Flask** that predicts the most suitable crop to grow based on soil nutrients and environmental conditions.  
It helps farmers and agriculture enthusiasts make data-driven decisions for better yield and sustainable farming.

---

## 🧠 Overview

The **Smart Crop Recommendation System** uses a trained **Machine Learning model** to suggest the best crop based on:
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

Once the user enters these values, the app predicts the most suitable crop and displays its image with a clean, modern interface.

---

## 🧰 Technology Stack

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Flask (Python)  
- **Machine Learning:** scikit-learn, pandas, numpy  
- **Model Storage:** joblib  
- **IDE:** Visual Studio Code  

---

## 📁 Project Structure

Smart_Crop/
├── app.py # Main Flask app
├── models/
│ └── crop_model.pkl # Trained ML model
├── data/
│ └── crop_dataset.csv # Dataset used for training
├── templates/
│ ├── index.html # Input page for user
│ └── result.html # Displays the recommended crop
├── static/
│ ├── css/
│ │ └── style.css # Custom styles
│ ├── images/
│ │ └── crop_images/ # Crop images (e.g., rice.jpg, wheat.jpg)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🌾 Project Screenshots
### 🔹 Images
<img src="static/images/demo%20cofe.jpg" alt="Home Page" width="600" height="350">
<img src="static/images/demo%20maize.jpg" alt="Home Page" width="600" height="350">
<img src="static/images/demo%20papaya.jpg" alt="Home Page" width="600" height="350">
<img src="static/images/demo%20pigeon.jpg" alt="Home Page" width="600" height="350">

## 🚀 Getting Started (Run Locally)

### 1.Clone the Repository

git clone https://github.com/sowjanya123-cpu/Smart_Crop.git
cd Smart_Crop

### 2.Create a Virtual Environment
python -m venv venv
venv\Scripts\activate     # For Windows

source venv/bin/activate  # For macOS/Linux

### 3.Install Dependencies
pip install -r requirements.txt

### 4.Run the Application
python app.py

### 5.🔗 Live Demo
https://smart-crop-anps.onrender.com/
