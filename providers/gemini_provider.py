import google.generativeai as genai
import os
from typing import List
from providers.base import EmbedderInterface

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

EMBED_MODEL = "models/embedding-001"

class GeminiEmbedder(EmbedderInterface):
    def embed(self, text: str) -> List[float]:
        if not text.strip():
            return []
        response = genai.embed_content(
            model=EMBED_MODEL,
            content=text,
            task_type="retrieval_document"
        )
        return response["embedding"]

    def batch_embed(self, texts: List[str]) -> List[List[float]]:
        return [self.embed(t) for t in texts if t.strip()]

# Export singleton instance
embedder = GeminiEmbedder()
