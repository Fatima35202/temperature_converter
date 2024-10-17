import streamlit as st
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title="Temperature Converter", layout="wide")

# Title and header
st.title("🌡️ Temperature Converter")
st.markdown("---")

# Sidebar with a nice header
with st.sidebar:
    st.header("Input Temperature")
    temp_unit = st.selectbox("Select the unit of temperature:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_value = st.number_input("Enter temperature value:", -273.15, 10000.0, 0.0)

    target_unit = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])

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

# Convert button with custom styling
if st.button("🔄 Convert"):
    converted_value = convert_temperature(temp_value, temp_unit, target_unit)
    st.success(f"✅ {temp_value} {temp_unit} is equal to **{converted_value:.2f} {target_unit}**")

# Add some CSS for styling
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #45a049; /* Darker green */
    }

    .reportview-container {
        background: linear-gradient(180deg, #f0f2f5 30%, #ffffff 100%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Fatima Tanveer")
