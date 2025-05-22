from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

# all-MiniLM-L6-v2 is back up plan if EMBEDDER_MODEL fails
model_choice = os.getenv("EMBEDDER_MODEL", "all-MiniLM-L6-v2")
truncate_dim = os.getenv("TRUNCATE_DIM")

if truncate_dim:
    truncate_dim = int(truncate_dim)
    print(f"Loading model '{model_choice}' with truncate_dim={truncate_dim}")
    model = SentenceTransformer(model_choice, device="cpu", truncate_dim=truncate_dim)
else:
    print(f"Loading model '{model_choice}'")
    model = SentenceTransformer(model_choice, device="cpu")
