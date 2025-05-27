# 🧠 RAG-as-a-Service | Retrieval-Augmented Generation App (LangChain + AWS Bedrock)

A fully-deployed, scalable RAG (Retrieval-Augmented Generation) application that leverages LangChain, Amazon Bedrock, and FastAPI to provide intelligent question-answering over your own data .

## 🔧 Tech Stack

- **LangChain** – LLM orchestration and retrieval logic
- **Amazon Bedrock** – Foundation model access (e.g., Anthropic Claude, Titan, or Llama 3)
- **Amazon S3** – Document storage and ingestion
- **Vector DB** – Document vector storage and similarity search with chromaDB
- **Amazon Lambda** – Serverless backend functions
- **API Gateway** – RESTful API with fastAPI
- **Amazon DynamoDB** – Session/metadata storage (optional)
- **Frontend** – basic CSS and HTML

---

## 🚀 Features

- ✅ Upload documents (PDFs, TXT, DOCX, etc.)
- ✅ Chunking, embedding, and vector storage
- ✅ Query interface powered by Bedrock-hosted LLMs
- ✅ Real-time retrieval and context injection (RAG)
- ✅ Streamed responses with token-level feedback (optional)
- ✅ Fully serverless and scalable backend on AWS
- ✅ Secure API with authentication options (API key/Cognito)

---


    F --> G[Generated Response]
    G --> H[Client]
