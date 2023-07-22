import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

st.title('BMI Calculator')

