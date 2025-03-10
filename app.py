# app.py
import streamlit as st

# Streamlit App Code
st.title("BMI Calculator")

# Input fields for weight and height
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, value=70.0)
height = st.number_input("Enter your height (in cm):", min_value=0.0, value=170.0)

# BMI Calculation
if st.button("Calculate BMI"):
    if height == 0:
        st.error("Height cannot be zero!")
    else:
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        # BMI Categories
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")