import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="centered"
)

# Title
st.markdown("<h1 style='text-align: center;'>💼 Salary Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict your salary based on experience</p>", unsafe_allow_html=True)

st.write("---")

# Input Section
st.subheader("📌 Enter Details")

experience = st.slider(
    "Years of Experience",
    min_value=0,
    max_value=30,
    value=1,
    step=1
)

# Predict Button
if st.button("🔍 Predict Salary"):
    prediction = model.predict(np.array([[experience]]))

    st.success(f"💰 Estimated Salary: ₹ {int(prediction[0])}")

# Extra UI Section
st.write("---")
st.subheader("📊 About Model")

st.info("""
- Model Used: Linear Regression  
- Input Feature: Years of Experience  
- Output: Predicted Salary  
""")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using Machine Learning</p>",
    unsafe_allow_html=True
)