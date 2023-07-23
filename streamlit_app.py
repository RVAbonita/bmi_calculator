import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
        height_meters = height / 100
        bmi = weight / (height_meters ** 2)
        return bmi
    except ValueError:
        return None

st.title('BMI Calculator 🏋️‍♂️')
st.write("Calculate your Body Mass Index (BMI)")

# Centering the title and header using CSS
st.markdown(
    """
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Input for weight and height in kilograms and centimeters
col1, col2 = st.columns(2)
with col1:
    weight = st.text_input('Enter your weight (kg)')
with col2:
    height = st.text_input('Enter your height (cm)')

# Calculate BMI
if st.button('Calculate BMI'):
    bmi_result = calculate_bmi(weight, height)
    if bmi_result is not None:
        st.write(f'Your BMI is: {bmi_result:.2f}')

        # Interpret BMI result
        if bmi_result < 18.5:
            st.warning('You are underweight.')
        elif 18.5 <= bmi_result < 24.9:
            st.success('You have a normal weight.')
        elif 25.0 <= bmi_result < 29.9:
            st.warning('You are overweight.')
        else:
            st.error('You are obese.')
    else:
        st.warning('Please enter valid numeric values for weight and height.')

# Centering the BMI Chart header using CSS
st.markdown(
    """
    <style>
    .centered-header {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# BMI Chart as a table
st.header('BMI Chart 📊',  class_='centered-header')
bmi_chart_data = {
    'BMI Category': ['Underweight', 'Normal weight', 'Overweight', 'Obese'],
    'BMI Range': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '>= 30.0'],
    'Interpretation': ['You are underweight.', 'You have a normal weight.', 'You are overweight.', 'You are obese.']
}
st.table(bmi_chart_data)

# Show the footer
st.write('---')
st.write('Created by Your Shir')
