import streamlit as st
import numpy as np
import time

st.title("Kaprekars Constant Attainer 🧮")

k = st.number_input(
    "**Enetr a number**", 1, 9999, None,
    help = "Four digit number. Except same four digit.",
    placeholder = "Click Generate to calculate with a random number"
)

if k == None:
    k = np.random.randint(10000)

# Center align buttons
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_button = st.button("**Generate**", use_container_width=True)


if generate_button:
    k_str = str(k).zfill(4) # leading zeros
    st.write("Checking for all same digits...")
    time.sleep(2)
    if k_str[0] == k_str[1] == k_str[2] == k_str[3]:
        st.warning(f" The number {k} have same four digits.", icon="⚠️")
        st.write("Retry.")
        st.stop()
    else:
        st.write("Good to go. 👍")
        k_desc = "".join(sorted(k_str, reverse = True))
        k_asc = "".join(sorted(k_str))
        st.write(k_desc, k_asc)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        retry_button = st.button("**Retry**", use_container_width=True)
