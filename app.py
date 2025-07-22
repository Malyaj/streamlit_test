import streamlit as st

# Initialize state
if "run" not in st.session_state:
    st.session_state.run = False

# Inputs
text = st.text_input("Enter your text")

# Action button
if st.button("Submit"):
    st.session_state.run = True  # Set flag to trigger processing

# Output only runs after button is pressed
if st.session_state.run:
    st.write("You entered:", text)
