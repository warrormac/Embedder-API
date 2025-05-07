from sentence_transformers import SentenceTransformer

# Load the embedding model once when the app starts
model = SentenceTransformer("all-MiniLM-L6-v2")  # Replace with your own if needed