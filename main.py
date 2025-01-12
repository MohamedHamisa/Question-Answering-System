from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from fastapi.security import APIKeyHeader
import os

app = FastAPI()

# Security
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != os.getenv("BACKEND_API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

# Load documents
def load_documents(file_path: str):
    if file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    elif file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        raise ValueError("Unsupported file format")
    return loader

# Initialize QA Chain
def initialize_qa_chain(file_path: str):
    loader = load_documents(file_path)
    index = VectorstoreIndexCreator().from_loaders([loader])
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
        chain_type="stuff",
        retriever=index.vectorstore.as_retriever()
    )
    return qa

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest, api_key: str = Depends(get_api_key)):
    try:
        qa = initialize_qa_chain("data.txt")  # Default dataset
        response = qa.run(request.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), api_key: str = Depends(get_api_key)):
    try:
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return {"message": "File uploaded successfully", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
