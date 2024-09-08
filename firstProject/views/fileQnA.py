import streamlit as st

st.title("File Related QnA")

uploaded_file = st.file_uploader("Browse File", type=["pdf", "docx", "txt"])
st.text_input("Ask Your Query")
if st.button("Summaries"):
        st.success("Summarising...")
