import streamlit as st

st.title("Temperature Converter")

st.sidebar.header("Input Temperature")

temp_unit = st.sidebar.selectbox("Select the unit of temperature:", ["Celsius", "Fahrenheit", "Kelvin"])
temp_value = st.sidebar.number_input("Enter temperature value:", -273.15, 10000.0, 0.0)

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value

    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value

    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

target_unit = st.sidebar.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

if st.sidebar.button("Convert"):
    converted_value = convert_temperature(temp_value, temp_unit, target_unit)
    st.success(f"{temp_value} {temp_unit} is equal to {converted_value:.2f} {target_unit}")
