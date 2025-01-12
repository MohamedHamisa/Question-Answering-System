import streamlit as st
import requests

st.title("LangChain Question Answering System")

# Input for user question
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question:
        # Call the FastAPI backend
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": question}
        )
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer found.")
            st.success(f"Answer: {answer}")
        else:
            st.error("Failed to get an answer. Please try again.")
    else:
        st.warning("Please enter a question.")
