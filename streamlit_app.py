import streamlit as st
import numpy as np
import time

# Main title
st.title("Kaprekar's Constant Attainer 🧮", anchor = False)

# Input number
k = st.number_input(
    "**Enetr a number**", 1, 9999, None,
    help = "Four digit number. Except same four digit.",
    placeholder = "Click Generate to calculate with a random number"
)

# Align buttons
col1, col2, col3, col4 = st.columns([1, 3, 1, 2])
with col1:
    generate_button = st.button("**Generate**", type = "primary", use_container_width=True)
with col4:
    st.link_button(
        label = "**What is Kaprekar's Constant?**",
        url = "https://en.wikipedia.org/wiki/6174",
        help = "wikipedia.org"
        )

# Generate button
if generate_button:

    # Generating random number if input is None
    if k == None:
        k = np.random.randint(10000)
        
        # simulate loading 
        with st.spinner("System is generating a random number..."):
            number = st.empty()
            time.sleep(1)
            number.write(k//1000)
            time.sleep(1)
            number.write(k//100)
            time.sleep(1)
            number.write(k//10)
            time.sleep(1)
            number.write(k)
            time.sleep(1)

    # placeholders for precess discriptions to be displayed
    placeholder = st.empty()

    # processing the number
    k_str = str(k).zfill(4) # leading zeros
    with st.spinner("Checking for all same digits..."):
        time.sleep(3)

    # checking for all same digits 
    if k_str[0] == k_str[1] == k_str[2] == k_str[3]:
        placeholder.write("")
        st.write("")
        st.warning(f"The number {k} have all the digits same.", icon="⚠️")

        # Retry button
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            retry_button = st.button("**Retry**", use_container_width=True)
        st.stop()
    else:
        placeholder.write("Atleast two different digits included. ✅")
        time.sleep(2)
        placeholder.write("")
        first_time = True
        last_time = False
        k_desc = "".join(sorted(k_str, reverse = True))
        k_asc = "".join(sorted(k_str))
        sub = int(k_desc) - int(k_asc)
        while True:
            if first_time:
                st.info("Sarting with " + k_str)
                first_time = False
            elif sub == 6174:
                last_time = True
                st.success("At last, taking " + str(int(k_desc) - int(k_asc)).zfill(4))
                k_str = str(int(k_desc) - int(k_asc)).zfill(4)
                k_desc = "".join(sorted(k_str, reverse = True))
                k_asc = "".join(sorted(k_str))
                sub = int(k_desc) - int(k_asc)
            else:
                st.info("Taking " + str(int(k_desc) - int(k_asc)).zfill(4))
                k_str = str(int(k_desc) - int(k_asc)).zfill(4)
                k_desc = "".join(sorted(k_str, reverse = True))
                k_asc = "".join(sorted(k_str))
                sub = int(k_desc) - int(k_asc)
            time.sleep(1)
            with st.spinner("Sorting in descending order..."):
                time.sleep(1)
            st.write("Decending order :", k_desc)
            with st.spinner("Sorting in ascending order..."):
                time.sleep(1)
            st.write("Ascending order : ", k_asc)
            sub = int(k_desc) - int(k_asc)
            with st.spinner("Subtracting ascending from descending..."):
                time.sleep(1)
            st.write("Subracted value : ", str(sub).zfill(4))
            st.write("-" * 50)
            time.sleep(1)
            if last_time:
                time.sleep(1)
                # st.info("The last two subtracted values are **6174**.\n\nSo the subtracted value will be the same for infinite times.")
                st.markdown("""
                    <h1 style='font-size:50px;'>
                        The last two subtracted values are 
                        <span style='color:green;'>6174</span>.<br>
                        So the subtracted value will be the same for &#8734; times.
                    </h1>
                """, unsafe_allow_html=True)

                time.sleep(5)

                st.markdown("""
                    <h1 style='font-size:50px;'>
                        Hence,<br><span style='color:red;'>Kaprekar's Constant - 6174</span><br>attained.
                    </h1>
                """, unsafe_allow_html=True)

                break
