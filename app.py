# app.py
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

selected = option_menu(
    menu_title="Heart Disease App",
    options=["Home", "Predict"],
    icons=["house", "heartbeat"],
    menu_icon="activity",
    default_index=0,
)

if selected == "Home":
    import Home
    Home.app()

elif selected == "Predict":
    import Predict
    Predict.app()
