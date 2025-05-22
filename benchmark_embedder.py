import os
import time
import argparse
import textwrap

from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

def extract_text(file_path):
    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

def chunk_text(text, max_chunk_length=800):
    if "\n\n" not in text:
        return textwrap.wrap(text, max_chunk_length)
    chunks = []
    current = ""
    for para in text.split("\n\n"):
        if len(current) + len(para) <= max_chunk_length:
            current += para + "\n\n"
        else:
            chunks.append(current.strip())
            current = para + "\n\n"
    if current:
        chunks.append(current.strip())
    return chunks

def benchmark(model_name, texts, truncate_dim=None):
    print(f"\n🔍 Benchmarking: {model_name} (truncate_dim={truncate_dim})")
    start = time.time()

    if truncate_dim:
        model = SentenceTransformer(model_name, device="cpu", truncate_dim=truncate_dim)
    else:
        model = SentenceTransformer(model_name, device="cpu")

    load_time = time.time()
    print(f"✅ Model loaded in {round(load_time - start, 2)}s")

    embeddings = model.encode(texts, batch_size=32, show_progress_bar=True)
    embed_time = time.time()

    print(f"✅ Encoded {len(texts)} texts in {round(embed_time - load_time, 2)}s")
    print(f"Total time: {round(embed_time - start, 2)}s")
    print(f"🔢 Embedding shape: {len(embeddings)} x {len(embeddings[0])}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to input .pdf or .txt file")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("❌ File not found.")
        exit()

    text = extract_text(args.file)
    chunks = chunk_text(text)
    print(f"📄 Extracted and chunked into {len(chunks)} segments")

    benchmark("all-MiniLM-L6-v2", chunks)
    benchmark("sentence-transformers/static-retrieval-mrl-en-v1", chunks, truncate_dim=384)


#To TEST
# python benchmark_embedder.py --file "path/to/your/document.pdf"
