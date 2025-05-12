from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from providers import (
    local_provider,
    openai_provider,
    gemini_provider,
    #anthropic_provider,
    #deepseek_provider,
    #qwen_provider
)
from dotenv import load_dotenv

load_dotenv()

EMBEDDERS = {
    "local": local_provider.embedder,
    "openai": openai_provider.embedder,
    "gemini": gemini_provider.embedder,
    #"anthropic": anthropic_provider.embedder,
    #"deepseek": deepseek_provider.embedder,
    #"qwen": qwen_provider.embedder
}

app = FastAPI()

class EmbedRequest(BaseModel):
    text: str
    provider: str = "local"

class EmbedResponse(BaseModel):
    embedding: List[float]

class BatchEmbedRequest(BaseModel):
    texts: List[str]
    provider: str = "local"

class BatchEmbedResponse(BaseModel):
    embeddings: List[List[float]]

@app.post("/embed", response_model=EmbedResponse)
def embed_text(request: EmbedRequest):
    try:
        embedder = EMBEDDERS.get(request.provider.lower(), local_provider.embedder)
        vector = embedder.embed(request.text)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_embed", response_model=BatchEmbedResponse)
def embed_batch(request: BatchEmbedRequest):
    try:
        provider = getattr(request, "provider", "local").lower()
        embedder = EMBEDDERS.get(provider, local_provider.embedder)
        vectors = embedder.batch_embed(request.texts)
        return {"embeddings": vectors}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))