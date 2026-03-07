# RAG-Based AI Document Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![RAG](https://img.shields.io/badge/AI-RAG-green)
![LLM](https://img.shields.io/badge/LLM-Gemini-orange)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered document assistant that enables **semantic search and question answering over PDF documents** using a **Retrieval-Augmented Generation (RAG)** pipeline. The system retrieves relevant document context using vector search and generates grounded responses using **Google Gemini**.

---

# Overview

This project implements an end-to-end **Retrieval-Augmented Generation (RAG)** system that allows users to query PDF documents using natural language.

The system consists of **two main pipelines**:

1️⃣ **Data Processing Pipeline** – responsible for document ingestion, chunking, embedding generation, and vector database storage.

2️⃣ **RAG Retrieval Pipeline** – retrieves relevant document chunks and generates grounded answers using a large language model.

---

# Demo

Example query:

<img width="785" height="269" alt="image" src="https://github.com/user-attachments/assets/30365d1d-7604-4ed1-abce-394394542d8a" />

---

# Features

- PDF document ingestion and preprocessing
- Text chunking using recursive text splitting
- Semantic embeddings using SentenceTransformers
- Vector-based semantic retrieval using ChromaDB
- Context-aware response generation using Google Gemini
- Source citations for grounded responses
- Retrieval evaluation using multiple test queries

---

# Tech Stack

- **Python**
- **LangChain utilities**
- **SentenceTransformers**
- **ChromaDB (Vector Database)**
- **Google Gemini API**
- **Jupyter Notebook**

---

# System Architecture

## 1. Data Processing Pipeline

```

PDF Documents
↓
Document Loading
↓
Text Chunking
↓
Embedding Generation
↓
Vector Database Storage (ChromaDB)

```

This pipeline prepares the documents for semantic search by converting them into embeddings and storing them in the vector database.

---

## 2. RAG Retrieval Pipeline

```

User Query
↓
Query Embedding
↓
Vector Similarity Search
↓
Top-K Relevant Chunks
↓
Context Construction
↓
Gemini LLM
↓
Answer Generation with Source Citations

```

This pipeline retrieves relevant document chunks and uses them as context for the LLM to generate accurate responses.

---

# Example Query

<img width="769" height="214" alt="image" src="https://github.com/user-attachments/assets/e8f8b633-c365-42f2-85d6-230c3af40b19" />

---

# Retrieval Evaluation

To evaluate the retrieval pipeline, multiple test queries were executed to ensure that the system retrieves the most relevant document sections before generating responses.

| Query | Retrieved Source | Result |
|------|------|------|
| What is attention function? | Attention_is_all_you_need.pdf | Relevant |
| what is an isolation forest model? | IEEE_Research_paper.pdf | Relevant |
| What is multi-attention function? | Attention_is_all_you_need.pdf | Relevant |
| what is random forest? | IEEE_Research_paper.pdf | Relevant |

The evaluation confirmed that the vector retrieval system correctly identifies semantically relevant document sections before generating answers.

---

# Project Structure

```

RAG_PROJECT
│
├── notebook
│   ├── document.ipynb
│   └── pdf_loader.ipynb
│
├── pdf_directory
│   ├── Attention_is_all_you_need.pdf
│   └── IEEE_Research_paper.pdf
│
├── data
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore

```

---

# Installation

### Clone the repository

```

git clone [https://github.com/yourusername/rag-document-assistant.git](https://github.com/yourusername/rag-document-assistant.git)
cd rag-document-assistant

```

### Install dependencies

```

pip install -r requirements.txt

```

### Add your API key

Create a `.env` file:

```

GEMINI_API_KEY=your_api_key_here

```

Run the notebook or pipeline to start querying documents.

---

# How It Works

1. PDF documents are loaded and processed.
2. Documents are split into smaller chunks for improved retrieval accuracy.
3. SentenceTransformers generate embeddings for each chunk.
4. The embeddings are stored in ChromaDB.
5. When a user asks a question, the retriever identifies the most relevant chunks.
6. The retrieved context is passed to Gemini to generate grounded answers.

---

