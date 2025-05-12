# 🧠 Embedder-API

The **Embedder-API** is a lightweight FastAPI service that exposes a REST endpoint for generating semantic embeddings using a local transformer model (e.g., SentenceTransformers). It is designed to be easily integrated into larger systems like Fast-S3Data, Milvus, or other document pipelines.

---

## 🚀 Features

- Accepts text or a list of texts via API
- Supports multiple providers: local, OpenAI, Gemini
- Returns vector embeddings (e.g., 384-dim)
- Runs locally — or via cloud APIs if configured
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
python-dotenv
```

Install them:

```bash
pip install -r requirements.txt
pip install uvicorn --user
```

---

## 🧠 Running the Server

From the project root:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8001
or
python -m uvicorn main:app --reload --port 8001
```

The server will be available at:  
👉 http://localhost:8001  
Swagger UI docs:  
👉 http://localhost:8001/docs

---

## 📥 Usage

### 1. `POST /embed`

Request:

```json
{
  "text": "Equimap builds modular AI pipelines.",
  "provider": "gemini"
}
```

### 2. `POST /batch_embed`

Request:

```json
{
  "texts": ["Chunk one.", "Chunk two."],
  "provider": "openai"
}
```

If no provider is specified, it defaults to `"local"`.

---

## 🧩 Architecture

```bash
Embedder-API/
├── main.py                      # FastAPI app (routes for /embed, /batch_embed)
├── config.py                    # Placeholder for central config
├── model_loader.py              # SentenceTransformer loader
├── .env                         # API keys
├── requirements.txt
└── providers/
    ├── base.py                  # EmbedderInterface
    ├── local_provider.py        # Local model (MiniLM)
    ├── openai_provider.py       # OpenAI embeddings
    ├── gemini_provider.py       # Gemini embeddings
    ├── anthropic_provider.py    # [placeholder]
    ├── deepseek_provider.py     # [placeholder]
    └── qwen_provider.py         # [placeholder]
```

---

## ✅ Current Functionality

- Dynamic provider selection from Fast-S3Data CLI
- Fully supports: `local`, `openai`, `gemini`
- Standardized interface with `.embed()` and `.batch_embed()` methods
- CLI prompts user for embedder (no code changes required)

---

## 🛠️ Roadmap

### ✅ Phase 0: Baseline Audit   (DONE)
- Extracted and reviewed code structure
- Verified provider wiring and CLI integration
- Established Embedder-API as a pluggable module

### ✅ Phase 1: Interface Standardization (DONE)
- Created `EmbedderInterface`
- Refactored `local`, `openai`, and `gemini` providers
- Aligned all routes with `.embed()` / `.batch_embed()`
- Added CLI provider selection for Fast-S3Data

### 🔄 Phase 2: Third-Party Gateway Support (ACTIVE)
- Integrate OpenRouter or LLM-Gateway
- Centralize API key management
- Unified routing to OpenAI, Gemini, Anthropic, DeepSeek, etc.

### 🧩 Phase 3: Mixed Use (Hybrid Embedding)
- Enable fallback from local → remote (or vice versa)
- Intelligent provider selection (based on size/cost)
- Allow partial remote embedding with priority config

### 🧠 Phase 4: Personal Model Integration
- Add loaders for GGUF, HuggingFace, Torch models
- Enable users to register their own local models
- Abstract path-to-model config mapping

---
## 🛠️ Left TODO

- Add OpenRouter / LLM-Gateway support (Phase 2)
- Add fallback for malformed/empty files
- Secure Embedder-API with API keys
- Expand local model support (e.g. Qwen, DeepSeek)
- Dockerize and deploy via Lambda/S3 trigger
- Add `/health` and logging endpoints
- Multi-tenant support and provider routing policies

---

## 📄 License

MIT License – use freely and contribute back!

---

## 🙋‍♂️ Maintainer

Created and maintained by **@warrormac**