import os
import requests
from typing import List
from providers.base import EmbedderInterface

class GatewayEmbedder(EmbedderInterface):
    def __init__(self):
        self.url = os.getenv("LLM_GATEWAY_URL", "http://localhost:7777/v1/embeddings")
        self.provider = "openai"

    def set_provider(self, provider_name):
        print("🛠️ [GATEWAY] LLM Provider set to:", provider_name)
        self.provider = provider_name

    def embed(self, text: str) -> List[float]:
        print("💡 [GATEWAY_PROVIDER] embed() was called")
        response = requests.post(self.url, json={
            "input": [text],
            "provider": self.provider
        })
        response.raise_for_status()
        return response.json()["data"][0]["embedding"]

    def batch_embed(self, texts: List[str]) -> List[List[float]]:
        print("💡 [GATEWAY_PROVIDER] batch_embed() was called")
        response = requests.post(self.url, json={
            "input": texts,
            "provider": self.provider
        })
        print("📤 [GATEWAY_PROVIDER] Response Status:", response.status_code)
        print("📤 [GATEWAY_PROVIDER] Response Body:", response.text)
        response.raise_for_status()
        return [item["embedding"] for item in response.json()["data"]]

embedder = GatewayEmbedder()
