import streamlit as st

st.title("Kaprekars Constant Attainer 🧮")

k = st.number_input("**Enetr a number**", 1, 9999, None, help = "Four digit number. Except same four digit.", placeholder = "Click Generate to calculate with a random number")