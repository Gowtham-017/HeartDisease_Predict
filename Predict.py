# Predict.py
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/heart_disease_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def app():
    st.title("🩺 Predict Heart Disease")
    st.write("Enter the following details:")

    # Collect inputs
    age = st.number_input("Age", 20, 100, 30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
    chol = st.number_input("Cholesterol (chol)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate (thalach)", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
    oldpeak = st.number_input("ST depression (oldpeak)", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope of ST segment", [0, 1, 2])
    ca = st.selectbox("Major vessels colored (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal", [0, 1, 2, 3])

    # Prepare input
    gender = 1 if sex == "Male" else 0
    input_data = np.array([[age, gender, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    input_scaled = scaler.transform(input_data)

    if st.button("Predict"):
        result = model.predict(input_scaled)[0]
        if result == 1:
            st.error("⚠️ The person is likely to have heart disease.")
        else:
            st.success("✅ The person is unlikely to have heart disease.")
