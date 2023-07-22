import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

st.title('BMI Calculator')

# Input for weight in kilograms
weight = st.number_input('Enter your weight (kg)', min_value=1.0, max_value=300.0, step=0.1)

# Input for height in centimeters
height = st.number_input('Enter your height (cm)', min_value=1.0, max_value=300.0, step=0.1)

# Calculate BMI
if st.button('Calculate BMI'):
    bmi_result = calculate_bmi(weight, height)
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

# Let's add a BMI chart for reference
st.header('BMI Chart')
st.image('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/bmi-chart.jpg', use_column_width=True)

# Show the footer
st.write('---')
st.write('Created by Your Name')
