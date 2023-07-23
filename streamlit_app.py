import streamlit as st


def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) based on weight and height.
    BMI = weight (kg) / (height (m) * height (m))
    """
    bmi = weight / (height * height)
    return bmi


def bmi_category(bmi):
    """
    Determine the BMI category based on the calculated BMI value.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    st.title("BMI Calculator 🏋️‍♂️")
    st.write("Calculate your Body Mass Index (BMI)")

    weight = st.number_input("Enter your weight in kilograms:", min_value=1.0, step=0.1)
    height = st.number_input("Enter your height in meters:", min_value=0.1, step=0.01)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        st.write(f"\nYour BMI is: {bmi:.2f}")
        st.write("Category:", category)

        st.subheader("BMI Chart")
        st.write("Category\tBMI Range")
        st.write("Underweight\t< 18.5")
        st.write("Normal weight\t18.5 - 24.9")
        st.write("Overweight\t25 - 29.9")
        st.write("Obese\t\t30 or greater")


if __name__ == "__main__":
    main()
