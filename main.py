from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from embedding import generate_embedding, generate_batch_embeddings

app = FastAPI()

class EmbedRequest(BaseModel):
    text: str

class EmbedResponse(BaseModel):
    embedding: List[float]

class BatchEmbedRequest(BaseModel):
    texts: List[str]

class BatchEmbedResponse(BaseModel):
    embeddings: List[List[float]]

@app.post("/embed", response_model=EmbedResponse)
def embed_text(request: EmbedRequest):
    try:
        vector = generate_embedding(request.text)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_embed", response_model=BatchEmbedResponse)
def embed_batch(request: BatchEmbedRequest):
    try:
        vectors = generate_batch_embeddings(request.texts)
        return {"embeddings": vectors}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))