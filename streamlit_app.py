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
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    generate_button = st.button("**Generate**", use_container_width=True)


if generate_button:

    placeholder = st.empty()

    k_str = str(k).zfill(4) # leading zeros
    with st.spinner("Checking for all same digits..."):
        time.sleep(3)
    if k_str[0] == k_str[1] == k_str[2] == k_str[3]:
        placeholder.write("")
        st.warning(f" The number {k} have all the digits same.", icon="⚠️")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            retry_button = st.button("**Retry**", use_container_width=True)
        st.stop()
    else:
        placeholder.write("Atleast two different digits included. 👍")
        time.sleep(1)
        st.info(f"Sarting with {k}")
        k_desc = int("".join(sorted(k_str, reverse = True)))
        k_asc = int("".join(sorted(k_str)))
        time.sleep(1)
        st.write("Decending order :", k_desc)
        st.write("Ascending order : ", k_asc)

