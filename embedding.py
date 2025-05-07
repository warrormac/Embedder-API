from model_loader import model

def generate_embedding(text: str):
    embedding = model.encode(text, show_progress_bar=False)
    return embedding.tolist()

def generate_batch_embeddings(texts: list):
    embeddings = model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    return embeddings.tolist()