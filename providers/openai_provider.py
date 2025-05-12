import openai
import os
from typing import List
from providers.base import EmbedderInterface

# Load from environment or fallback (you can remove the fallback in production)
openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

EMBED_MODEL = "text-embedding-3-small"

class OpenAIEmbedder(EmbedderInterface):
    def embed(self, text: str) -> List[float]:
        if not text.strip():
            return []
        response = openai.Embedding.create(
            input=[text],
            model=EMBED_MODEL
        )
        return response["data"][0]["embedding"]

    def batch_embed(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        response = openai.Embedding.create(
            input=texts,
            model=EMBED_MODEL
        )
        return [item["embedding"] for item in sorted(response["data"], key=lambda x: x["index"])]

# Export singleton instance
embedder = OpenAIEmbedder()
