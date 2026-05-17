import streamlit as st
import math
import requests

st.set_page_config(page_title="🧮 Advanced Calculator", page_icon="🧠")
st.title("🧮 Advanced Calculator with Extra Tools")
st.markdown("Perform advanced calculations, currency conversions, and discounts.")

# ----------- Basic Calculator -----------
st.header("🧠 Calculator")
num1 = st.number_input("Enter first number")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm"])
num2 = None

if operation not in ["Square Root", "Logarithm"]:
    num2 = st.number_input("Enter second number")

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Cannot divide by 0"
        elif operation == "Power":
            result = math.pow(num1, num2)
        elif operation == "Square Root":
            result = math.sqrt(num1)
        elif operation == "Logarithm":
            result = math.log(num1)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# ----------- Discount Calculator -----------
st.header("🎯 Discount Calculator")
amount = st.number_input("Enter original amount", min_value=0.0, format="%.2f")
discount_percent = st.slider("Select discount %", 0, 100, step=5)

if st.button("Calculate Discount"):
    discount_value = amount * discount_percent / 100
    final_price = amount - discount_value
    st.info(f"Discounted Price: {final_price:.2f}")
    st.caption(f"You saved: {discount_value:.2f}")

# ----------- Currency Converter -----------
st.header("💱 Currency Converter (Fixed Rates Example)")
currencies = {
    "USD": 1.00,
    "EUR": 0.90,
    "PKR": 277.50,
    "INR": 83.30,
    "GBP": 0.78,
    "CAD": 1.36,
    "AUD": 1.51
}

from_curr = st.selectbox("From", currencies.keys(), key="from")
to_curr = st.selectbox("To", currencies.keys(), key="to")
amount_curr = st.number_input("Amount to convert", min_value=0.0, format="%.2f")

if st.button("Convert Currency"):
    try:
        usd_amount = amount_curr / currencies[from_curr]
        converted_amount = usd_amount * currencies[to_curr]
        st.success(f"{amount_curr:.2f} {from_curr} = {converted_amount:.2f} {to_curr}")
    except Exception as e:
        st.error(f"Conversion error: {e}")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
