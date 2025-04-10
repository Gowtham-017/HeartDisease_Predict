# Home.py
import streamlit as st

def app():
    st.title("❤️ Heart Disease Prediction App")
    st.write("""
    This app uses **Machine Learning** to predict the possibility of heart disease based on your basic medical details.
    
    Navigate to the **Predict** page to enter your information and get instant results.
    """)

    st.subheader("🩺 Features Used for Prediction")

    st.markdown("""
    - **Age**: Risk increases significantly after 45 (men) or 55 (women).
    - **Sex**: Men have higher early risk; women catch up post-menopause.
    - **Chest Pain Type (cp)**: Chest discomfort or pain may signal reduced blood flow to the heart.
    - **Resting Blood Pressure (trestbps)**: Consistently high values can strain the heart and arteries.
    - **Cholesterol Level (chol)**: High cholesterol can lead to plaque buildup in arteries.

    These features allow early risk screening to prompt timely medical attention.
    """)

    with st.expander("💡 Heart Health Tips"):
        st.markdown("""
        - 🥗 **Eat heart-friendly foods**: Focus on fruits, vegetables, whole grains, and healthy fats.
        - 🚶 **Stay active**: Just 30 minutes of brisk walking a day can improve cardiovascular health.
        - 🚭 **Avoid smoking**: Smoking significantly increases heart disease risk.
        - 😌 **Manage stress**: Chronic stress may damage arteries and raise blood pressure.
        - 💧 **Stay hydrated** and maintain a healthy weight.
        - 🔍 **Get regular checkups** — early detection can save lives!
        """)


    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 14px;'>"
        "© 2025 Heart Disease Predictor | Built with ❤️ using Streamlit & Machine Learning"
        "</div>",
        unsafe_allow_html=True
    )
