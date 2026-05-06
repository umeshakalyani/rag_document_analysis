# RAG Document Analysis Platform

AI-powered document analysis platform using Retrieval-Augmented Generation (RAG), FastAPI, OpenAI, and ChromaDB.

---

# Project Overview

This project allows users to:

- Upload PDF and DOCX documents
- Extract and process document text
- Generate embeddings using AI models
- Store vectors in ChromaDB
- Ask questions about uploaded documents
- Get AI-generated contextual answers using RAG architecture

This system simulates real-world enterprise AI document assistants like:
- Google NotebookLM
- Microsoft Copilot
- OpenAI Retrieval Systems

---

# Features

- PDF Upload
- DOCX Upload
- Text Extraction
- Text Chunking
- Embedding Generation
- Vector Database Storage
- AI Question Answering
- Semantic Search
- FastAPI Backend
- Swagger API Documentation

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## AI/ML
- OpenAI GPT-4o-mini
- Sentence Transformers
- RAG Architecture

## Database
- ChromaDB (Vector Database)

## Document Processing
- PyPDF
- python-docx

---

# Folder Structure

```bash
rag-document-analysis/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/rag_document_analysis.git
```

## Move Into Project

```bash
cd rag_document_analysis
```

---

# Backend Setup

## Move to Backend

```bash
cd backend
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` inside backend folder.

```env
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

Open:

```bash
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload Document

```http
POST /upload
```

Supports:
- PDF
- DOCX

---

## Ask Questions

```http
POST /chat
```

Example:

```json
{
  "question": "What is this document about?"
}
```

---

# AI Workflow

```text
Upload Document
      ↓
Extract Text
      ↓
Chunk Text
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
Ask Questions
      ↓
Retrieve Relevant Chunks
      ↓
Generate AI Answer
```

---

# Future Improvements

- React Frontend
- JWT Authentication
- PostgreSQL Integration
- Docker Deployment
- AWS Deployment
- Multi-Document Support
- OCR Support
- Streaming AI Responses
- LangChain Integration

---

# Use Cases

- Resume Analysis
- Legal Document Assistant
- Research Paper Chatbot
- Enterprise Knowledge Base
- AI Study Assistant
- HR Policy Assistant

---

# Author

## Umesha
Data Science Engineering Student

---

# License

This project is for educational and portfolio purposes.
