# 🧠 Embedder-API

The **Embedder-API** is a lightweight FastAPI service that exposes a REST endpoint for generating semantic embeddings using a local transformer model (e.g., SentenceTransformers). It is designed to be easily integrated into larger systems like Fast-S3Data, Milvus, or other document pipelines.

---

## 🚀 Features

- Accepts text or a list of texts via API
- Returns vector embeddings (e.g., 384-dim)
- Runs locally — no external model API calls
- Designed to support GPU acceleration (if hardware is available)
- Easy integration with CLI tools or pipelines (e.g., Fast-S3Data)

---

## 📦 Requirements

- Python 3.8+
- pip

### 🔧 Dependencies (from `requirements.txt`)

```
fastapi
uvicorn
sentence-transformers
pydantic
```

Install them:

```bash
pip install -r requirements.txt
```

---

## 🧠 Running the Server

From the project root:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
```

The server will be available at:  
👉 [http://localhost:8001](http://localhost:8001)

Swagger UI docs:  
👉 [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 📥 Usage

### 1. `POST /embed`

Request:

```json
{
  "text": "Equimap builds modular AI pipelines."
}
```

Response:

```json
{
  "embedding": [0.123, 0.456, ...]
}
```

---

### 2. `POST /batch_embed`

Request:

```json
{
  "texts": [
    "Paragraph one.",
    "Paragraph two.",
    "Paragraph three."
  ]
}
```

Response:

```json
{
  "embeddings": [
    [ ... ], [ ... ], [ ... ]
  ]
}
```

---


## 📄 License

MIT License – use freely and contribute back!

---

## 🙋‍♂️ Maintainer

Created and maintained by **@warrormac**
