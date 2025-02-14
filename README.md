# 6174
This Streamlit web app demonstrates the Kaprekar's Constant process. Given a four-digit number (excluding numbers with all identical digits), the app performs iterative calculations to reach Kaprekar's Constant (6174) using Kaprekar's routine. The app also includes smooth UI effects, background customization, and real-time processing animations.

## Features & Functionality
- User Input & Random Generation
    - Users can enter a four-digit number manually.
    - If no number is entered, the app generates a random four-digit number.
- Validation Check
    - The app checks if all digits of the number are the same (e.g., 1111, 5555).
    - If the number is invalid, the app displays a warning and allows the user to retry.
- Kaprekar’s Routine Execution
    - The app performs iterative steps to reach 6174:
    - Sort digits in descending order.
    - Sort digits in ascending order.
    - Subtract the smaller number from the larger number.
    - Repeat until the result becomes 6174.
- Smooth UI & Loading Effects
    - Uses st.spinner() and time.sleep() to create real-time progress animations.
    - Displays steps one-by-one to make the process interactive.
    - Uses CSS animations to enhance the experience.
## Visual Enhancements
- 🎨 Custom Background
    - The app sets a background image from a URL using CSS.
    - Applies a semi-transparent white overlay to improve readability.
- 📌 Typography & Formatting
    - Uses HTML & CSS inside st.markdown() to control font size, colors, and effects.
    - Highlights important numbers and text using colors (green for 6174, red for Kaprekar's Constant).
- ⌛ Smooth Transitions & Animations
    - st.spinner() adds loading indicators for sorting, subtracting, and checking conditions.
    - Step-by-step display ensures the user experiences the calculation dynamically.

## ❔ What is 6174
Refer to the [Wikipedia documentation on Kaprekar's Constant](https://en.wikipedia.org/wiki/6174) for more details.

## Demo App
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kaprekars.streamlit.app/)
## Live Preview  
[![Kaprekar's Constant Attainer](https://img.shields.io/badge/Open-App-brightgreen)](https://kaprekars.streamlit.app/)


