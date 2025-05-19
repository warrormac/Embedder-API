from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from providers import (
    local_provider,
    gateway_provider
)
from providers.router import EmbedderRouter
from dotenv import load_dotenv

load_dotenv()

EMBEDDERS = {
    "local": local_provider.embedder,
    "gateway": gateway_provider.embedder,
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
        router = EmbedderRouter(strategy=request.provider)
        result = router.embed(request.text)

        if isinstance(result, dict):  # case: "both"
            return {"embedding": result.get("local") or result.get("gateway")}
        return {"embedding": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/batch_embed", response_model=BatchEmbedResponse)
def embed_batch(request: BatchEmbedRequest):
    try:
        router = EmbedderRouter(strategy=request.provider)
        result = router.batch_embed(request.texts)

        if isinstance(result, dict):  # strategy="both"
            return {"embeddings": result.get("local") or result.get("gateway")}
        return {"embeddings": result}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

