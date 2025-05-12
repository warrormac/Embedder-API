from model_loader import model
from providers.base import EmbedderInterface

class LocalEmbedder(EmbedderInterface):
    def embed(self, text: str):
        return model.encode(text, show_progress_bar=False).tolist()

    def batch_embed(self, texts: list):
        return model.encode(texts, show_progress_bar=False, convert_to_numpy=True).tolist()

# Export an instance
embedder = LocalEmbedder()
