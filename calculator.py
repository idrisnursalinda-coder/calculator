import streamlit as st

st.title("Division Calculator")
st.write("Enter two numbers to perform division")

col1, col2 = st.columns(2)

with col1:
    num1 = st.text_input("Enter first number:")
with col2:
    num2 = st.text_input("Enter second number:")

if st.button("Divide", type="primary"):
    if not num1 or not num2:
        st.warning("Please enter both numbers")
    else:
        try:
            n1 = float(num1)
            n2 = float(num2)
            result = n1 / n2
            st.success(f"✅ Result: {n1} ÷ {n2} = {result}")
        except ValueError:
            st.error("❌ Invalid input! Please enter numeric values only.")
        except ZeroDivisionError:
            st.error("❌ Cannot divide by zero! Please enter a non-zero divisor.")