import streamlit as st

# Streamlit UI
st.title("Model Deployment with Streamlit")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
