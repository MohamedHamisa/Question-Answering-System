---

# **LangChain Question Answering System**

*A Question Answering System built with LangChain, FastAPI (backend), and Streamlit (frontend).*

---

## **Features**

- **Backend**: FastAPI server with LangChain integration for question answering.
- **Frontend**: Streamlit app for user interaction.
- **Customizable**: Add your own dataset or modify the LangChain pipeline.
- **Docker Support**: Easily deploy the app using Docker.

---

## **Prerequisites**

Before running the project, ensure you have the following installed:

- **Python 3.9 or higher**
- **Pip** (Python package manager)
- **Git**
- **Docker** (optional, for containerization)

---

## **Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/langchain-app.git
cd langchain-app
```

### **2. Set Up the Backend**

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key:
   - Replace `"your-openai-api-key"` in `backend/main.py` with your actual OpenAI API key.

4. Add your dataset:
   - Place your text data in a file named `data.txt` in the `backend` folder.

5. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```
   *The backend will be available at `http://localhost:8000`.*

---

### **3. Set Up the Frontend**

1. Navigate to the `frontend` folder:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   *The frontend will be available at `http://localhost:8501`.*

---

## **Docker Setup**

If you prefer to run the app using Docker:

1. Build the Docker images:
   ```bash
   docker build -t langchain-backend -f Dockerfile .
   docker build -t langchain-frontend -f Dockerfile .
   ```

2. Run the backend container:
   ```bash
   docker run -d -p 8000:8000 langchain-backend
   ```

3. Run the frontend container:
   ```bash
   docker run -d -p 8501:8501 langchain-frontend
   ```

4. Access the app:
   - **Backend**: `http://localhost:8000`
   - **Frontend**: `http://localhost:8501`

---

## **Project Structure**

```
langchain-app/
│
├── backend/
│   ├── main.py               # FastAPI backend
│   ├── requirements.txt      # Backend dependencies
│   └── data.txt              # Sample dataset
│
├── frontend/
│   ├── app.py                # Streamlit frontend
│   └── requirements.txt      # Frontend dependencies
│
├── .gitignore                # Files to ignore in Git
├── README.md                 # Project documentation
└── Dockerfile                # Docker configuration
```

---

## **How It Works**

1. The user enters a question in the Streamlit frontend.
2. The frontend sends the question to the FastAPI backend.
3. The backend uses LangChain and OpenAI to generate an answer based on the provided dataset.
4. The answer is sent back to the frontend and displayed to the user.

---

## **Customization**

- **Dataset**: Replace `data.txt` with your own dataset.
- **LangChain Pipeline**: Modify the `RetrievalQA` chain in `backend/main.py` to use different models or configurations.
- **API Endpoints**: Add more endpoints to the FastAPI backend for additional functionality.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **License**

This project is licensed under the **MIT License**.

---

## **Acknowledgments**

- **[LangChain](https://www.langchain.com/)** for the powerful NLP framework.
- **[OpenAI](https://openai.com/)** for the GPT models.
- **[FastAPI](https://fastapi.tiangolo.com/)** for the backend.
- **[Streamlit](https://streamlit.io/)** for the frontend.

---

