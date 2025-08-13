# calculator.py
# pip install streamlit
# This is a simple calculator app using Streamlit
# Run the app with: streamlit run calculator.py
import streamlit as st

st.title("Simple Calculator")
st.markdown("Welcome to my first web calculator app using Streamlit!")
c1, c2 = st.columns(2)
fnum1 = c1.number_input("first number", value=0)
fnum2 = c2.number_input("second number", value=0)
options = ["Addition", "Subtraction", "Multiplication", "Division"]
choice = st.radio("Select operation", options)
button = st.button("Calculate")
result = 0
st.success(f'Result is: {result}')