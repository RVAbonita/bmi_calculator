import streamlit as st

# Function to convert height from feet and inches to centimeters
def convert_to_cm(height_str):
    try:
        feet, inches = map(int, height_str.split("'"))
        height_cm = feet * 30.48 + inches * 2.54
        return height_cm
    except ValueError:
        return None

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

st.title('BMI Calculator')

# Input for weight in kilograms
weight = st.number_input('Enter your weight (kg)', min_value=1.0, max_value=300.0, step=None)

# Input for height in feet and inches
height_str = st.text_input('Enter your height (e.g., 5\'5")')

# Convert height to centimeters
height_cm = convert_to_cm(height_str)

# Calculate BMI
if st.button('Calculate BMI'):
    if height_cm is not None:
        bmi_result = calculate_bmi(weight, height_cm)
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
        st.warning("Please enter your height in the format 'feet'inches\", for example, 5'5\".")

# BMI Chart as a table
st.header('BMI Chart')
bmi_chart_data = {
    'BMI Category': ['Underweight', 'Normal weight', 'Overweight', 'Obese'],
    'BMI Range': ['< 18.5', '18.5 - 24.9', '25.0 - 29.9', '>= 30.0'],
    'Interpretation': ['You are underweight.', 'You have a normal weight.', 'You are overweight.', 'You are obese.']
}
st.table(bmi_chart_data)

# Show the footer
st.write('---')
st.write('Created by Shir')
