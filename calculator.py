import streamlit as st

st.title("Division Calculator")
col1, col2 = st.columns(2)

with col1:
    num1 = st.text_input("Enter first number:")
with col2:
    num2 = st.text_input("Enter second number:")

if st.button("Calculate"):
    try:
        n1 = float(num1)
        n2 = float(num2)
        result = n1 / n2
        st.success(f"Result: {result}")
    except ValueError:
        st.error("Invalid input! Please enter numeric values.")
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero!")