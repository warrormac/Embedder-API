# 🧠 Embedder-API

The **Embedder-API** is a modular FastAPI service for generating semantic embeddings. It supports local models, remote APIs via a self-hosted gateway, or both concurrently, with batch processing and fallback logic. Built to plug into larger document pipelines like Fast-S3Data or any vector database workflow.

---

## 🚀 Features

- Accepts single or batch input via `/embed` and `/batch_embed`
- Provider selection: `local`, `gateway`, or `both`
- Dual-path fallback with status feedback when using `both`
- Full support for OpenAI, Gemini via LLM-Gateway
- Unified `EmbedderInterface` with `.embed()` and `.batch_embed()` methods
- Works out-of-the-box with Fast-S3Data CLI
- GPU acceleration supported (if available)

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
├── main.py                      # FastAPI app
├── config.py                    # Central config
├── model_loader.py              # Local model handler
├── .env                         # API keys
├── requirements.txt
└── providers/
    ├── base.py                  # EmbedderInterface
    ├── local_provider.py        # Local model (e.g., MiniLM)
    ├── gateway_provider.py      # LLM-Gateway handler
    ├── openai_provider.py       # OpenAI direct API
    ├── gemini_provider.py       # Gemini embeddings
    ├── anthropic_provider.py    # [placeholder]
    ├── deepseek_provider.py     # [placeholder]
    └── router.py                # Dynamic routing logic
```

---

## ✅ Capabilities Summary

- Provider options: `local`, `gateway`, `both`
- Full batch support: `batch_embed()`
- Resilient fallback logic in `"both"` mode
- Plug-and-play CLI integration
- FastAPI, async-ready, modular

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

## 📄 License

MIT License – use freely and contribute back!

---

## 🙋‍♂️ Maintainer

Created and maintained by **@warrormac**
