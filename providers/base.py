from abc import ABC, abstractmethod
from typing import List

class EmbedderInterface(ABC):
    @abstractmethod
    def embed(self, text: str) -> List[float]:
        """Embed a single string"""
        pass

    @abstractmethod
    def batch_embed(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of strings"""
        pass
