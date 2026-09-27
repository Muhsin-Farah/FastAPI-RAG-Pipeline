
A production-grade, containerized Retrieval-Augmented Generation (RAG) microservice built with FastAPI, LangChain, and Docker. This project implements a robust backend architecture designed to ingest local knowledge bases, execute local HuggingFace embedding calculations, and integrate cloud-based LLM inference via OpenRouter with strict Pydantic JSON schema validation. This pipeline is adapted from the TensorTonic project section where you can find it but with To Do sections to complete the Project.

This implementation leverages the TensorTonics existing RAG pipeline architecture, adapting it for scalable deployment, reliable error handling, and high-performance asynchronous API routing.

Technical Highlights & Engineering Stack
Backend & API Architecture:

Developed asynchronous REST endpoints (/predict, /query) using FastAPI with strict input/output serialization via Pydantic.

Implemented robust exception handling and fallback routing mechanisms to gracefully manage upstream API latency and rate limits.

Retrieval-Augmented Generation (RAG):

Powered by LangChain for document chunking, vector store orchestration, and contextual prompt construction.

Employs local sentence embeddings (all-MiniLM-L6-v2) via HuggingFace for efficient vector representation and semantic search.

Cloud LLM Integration:

Integrates with OpenRouter using an OpenAI-compatible client wrapper, leveraging dynamic model auto-routing (openrouter/free) for resilient, zero-cost production inference.

Containerization & Deployment:

Fully containerized using Docker with optimized multi-layer builds, ensuring consistent environment parity across development and production servers.
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
``````
API Specification
POST /predict
Accepts a user query, queries the local vector store for relevant context chunks, and returns a strict JSON-validated response.

Request Body:

JSON
{
  "question": "What is the document about?"
}
Response Body (200 OK):
````
JSON
{
  "answer": "The document contains details regarding...",
  "source_ids": [
    "app/document.txt"
  ]
}
``````

Local Development & Setup
1. Clone the Repository
Bash
git clone [https://github.com/Muhsin-Farah/FastAPI-RAG-Pipeline.git](https://github.com/Muhsin-Farah/FastAPI-RAG-Pipeline.git)
cd FastAPI-RAG-Pipeline
2. Build and Run via Docker
Build the local container image and run the application, passing your OpenRouter API key as an environment variable:

PowerShell
# Build the Docker image
docker build -t mymodel-rag .

# Run the container instance
docker run -d -p 8000:8000 `
  -e OPENAI_API_KEY="your_openrouter_api_key_here" `
  -e OPENAI_BASE_URL="[https://openrouter.ai/api/v1](https://openrouter.ai/api/v1)" `
  --name my-rag-container `
  mymodel-rag

3. Interactive Documentation
Once the container is running, access the interactive Swagger UI in your browser to test endpoints live:

URL: http://localhost:8000/docs
