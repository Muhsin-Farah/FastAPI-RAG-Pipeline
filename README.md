FastAPI RAG Pipeline
A production-ready Retrieval-Augmented Generation (RAG) backend service built with FastAPI, LangChain, and Docker, utilizing OpenRouter for cloud LLM inference and local HuggingFace embeddings for secure, efficient document processing.

Architecture & Tech Stack
Framework: FastAPI (Async API routing, Pydantic validation)

Orchestration & RAG: LangChain (Vector store, text chunking, prompt chaining)

Embeddings: HuggingFace Sentence Transformers (all-MiniLM-L6-v2 running locally)

LLM Provider: OpenRouter API (Auto-routing free-tier inference via OpenAI client wrapper)

Containerization: Docker (Multi-stage build optimized for local/cloud deployment)
````
RAG/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entrypoint and routes
│   ├── rag.py           # Core RAG pipeline, vector store, and LLM setup
│   └── document.txt     # Ingested knowledge base source
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
└── README.md
