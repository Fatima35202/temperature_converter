%%writefile app.py
import streamlit as st

# Title of the app
st.title("Temperature Converter")

# Create a sidebar for input
st.sidebar.header("Input Temperature")

# Select temperature unit
temp_unit = st.sidebar.selectbox("Select the unit of temperature:", ["Celsius", "Fahrenheit", "Kelvin"])

# Input temperature value
temp_value = st.sidebar.number_input("Enter temperature value:", -273.15, 10000.0, 0.0)

# Conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value  # Celsius to Celsius

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value  # Fahrenheit to Fahrenheit

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Kelvin to Kelvin

# Select target unit for conversion
target_unit = st.sidebar.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

# Perform conversion
if st.sidebar.button("Convert"):
    converted_value = convert_temperature(temp_value, temp_unit, target_unit)
    st.success(f"{temp_value} {temp_unit} is equal to {converted_value:.2f} {target_unit}")

# Add some styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f5;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
