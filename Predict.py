# Predict.py
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model/heart_disease_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def app():
    st.title("🩺 Predict Heart Disease")
    st.write("Enter the following details:")

    age = st.number_input("Age", min_value=16, max_value=100, step=1, format="%d")
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (trestbps)", step=1, format="%d")
    chol = st.number_input("Cholesterol (chol)", step=1, format="%d")


    # Prepare input
    gender = 1 if sex == "Male" else 0
    input_data = np.array([[age, gender, cp, trestbps, chol]])
    input_scaled = scaler.transform(input_data)

    if st.button("Predict"):
        result = model.predict(input_scaled)[0]
        if result == 1:
            st.error("⚠️ The person is likely to have heart disease.")
        else:
            st.success("✅ The person is unlikely to have heart disease.")
