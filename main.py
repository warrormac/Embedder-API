from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from providers import (
    local_provider,
    gateway_provider
)
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
        embedder = EMBEDDERS.get(request.provider.lower(), local_provider.embedder)
        vector = embedder.embed(request.text)
        return {"embedding": vector}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_embed", response_model=BatchEmbedResponse)
def embed_batch(request: BatchEmbedRequest):
    try:
        provider = getattr(request, "provider", "local").lower()
        embedder = EMBEDDERS.get(provider, local_provider)

        # 👇 Extract llm_provider if gateway was selected
        llm_provider = getattr(request, "llm_provider", None)
        if provider == "gateway" and llm_provider:
            embedder.set_provider(llm_provider)

        print("🔍 [MAIN] Resolved provider:", provider)
        print("🔍 [MAIN] Using embedder object:", embedder.__class__.__name__)

        vectors = embedder.batch_embed(request.texts)
        return {"embeddings": vectors}
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

