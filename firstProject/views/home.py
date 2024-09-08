import streamlit as st

# Title and Subtitle
st.markdown("<h1 style='font-size:36px;'>Ask Your Query</h1>", unsafe_allow_html=True)
query = st.text_input("Your Query", label_visibility="hidden")
st.markdown("<h3 style='font-size:18px;'>Calling LLM...</h3>", unsafe_allow_html=True)

# Input and output areas

response = st.text_area("Response")
# Place the logout button