from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import RAGPipeline

app = FastAPI(
    title="FastAPI RAG Pipeline",
    description="RAG endpoint using local embeddings and OpenRouter LLM inference."
)

# Initialize RAG Pipeline at startup
rag_pipeline = RAGPipeline("app/document.txt")


# Request Payload Model
class PredictRequest(BaseModel):
    question: str
    k: Optional[int] = 3


# Response Payload Model matching target schema
class PredictResponse(BaseModel):
    answer: str
    source_ids: List[str]


@app.get("/")
def read_root():
    return {"message": "RAG API is running."}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    try:
        # Call RAG pipeline with keyword parameters matching rag.py
        result = rag_pipeline.generate_answer(
            query=payload.question,
            k=payload.k if payload.k is not None else 3
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal RAG pipeline error: {str(e)}"
        )


@app.post("/query", response_model=PredictResponse)
def query(payload: PredictRequest):
    # Secondary endpoint routing to the same pipeline method
    return predict(payload)