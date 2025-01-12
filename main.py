from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

app = FastAPI()

# Load documents (you can replace this with your own data)
loader = TextLoader("data.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(api_key="your-openai-api-key"),
    chain_type="stuff",
    retriever=index.vectorstore.as_retriever()
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    try:
        response = qa.run(request.question)
        return {"answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
