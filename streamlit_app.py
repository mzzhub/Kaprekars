import streamlit as st
import numpy as np

st.title("Kaprekars Constant Attainer 🧮")

k = st.number_input(
    "**Enetr a number**", 1, 9999, None,
    help = "Four digit number. Except same four digit.",
    placeholder = "Click Generate to calculate with a random number"
)

if k == None:
    k = np.random.randint(10000)

if st.button("**Generate**"):
    k_str = str(k)
    if k_str[0] == k_str[1] == k_str[2] == k_str[3]:
        st.write("Break")
        