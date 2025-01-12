import streamlit as st
import requests
import os

# Streamlit App
st.title("LangChain Question Answering System")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter your API Key", type="password")
    model_temperature = st.slider("Model Temperature", 0.0, 1.0, 0.7)

# File Upload
uploaded_file = st.file_uploader("Upload a file (TXT or PDF)", type=["txt", "pdf"])
if uploaded_file:
    file_path = f"uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File uploaded successfully: {uploaded_file.name}")

# Input for user question
question = st.text_input("question?")

if st.button("Get Answer"):
    if question and api_key:
        try:
            # Call the FastAPI backend
            response = requests.post(
                "http://localhost:8000/ask",
                json={"question": question},
                headers={"X-API-KEY": api_key}
            )
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.success(f"**Answer:** {answer}")
            else:
                st.error(f"Failed to get an answer. Error: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question and provide a valid API Key.")
