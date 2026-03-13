# RAG-Based AI Document Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![VectorDB](https://img.shields.io/badge/VectorDB-ChromaDB-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-SentenceTransformers-yellow)
![LLM](https://img.shields.io/badge/LLM-Google%20Gemini-green)
![Architecture](https://img.shields.io/badge/Architecture-RAG-purple)
---

# RAG-Based AI Document Assistant

A **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions about PDF documents and receive context-aware answers powered by a Large Language Model.

The system processes research papers, converts them into vector embeddings, stores them in a vector database, retrieves relevant context, and generates answers using an LLM.

This project demonstrates the **core architecture used in modern Generative AI applications**, including document ingestion, semantic search, vector databases, and LLM-based response generation.

---

# Overview

Large Language Models are powerful but limited to the data they were trained on.

This project implements **Retrieval-Augmented Generation (RAG)**, a technique that improves LLM responses by retrieving relevant information from external documents.

Instead of relying solely on the model’s training knowledge, the system retrieves relevant document sections and uses them as context for generating answers.

This enables AI systems to answer questions based on **private knowledge bases such as research papers, reports, or internal documentation**.

---

# Architecture

User Query

↓

Retriever

↓

Vector Database (ChromaDB)

↓

Relevant Document Chunks

↓

LLM (Gemini)

↓

Generated Answer + Sources

---

# System Diagram

```
                ┌─────────────────────┐
                │     User Query      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │      Retriever      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │   Vector Database   │
                │      ChromaDB       │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Relevant PDF Chunks │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │     Gemini LLM      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │  Generated Answer   │
                │    + Sources        │
                └─────────────────────┘
```

---

# Project Structure

```
RAG-Based-AI-Document-Assistant
│
├── app.py                 # Streamlit frontend
├── rag_pipeline.py        # RAG orchestration logic
├── retriever.py           # Vector search and retrieval logic
├── vector_store.py        # ChromaDB vector database management
├── embeddings.py          # SentenceTransformer embedding model
├── data_ingestion.py      # PDF loading and document chunking
├── requirements.txt
├── README.md
│
└── data/
    └── pdfs/              # Source PDF documents
```
 IN VSCODE

 <img width="258" height="326" alt="image" src="https://github.com/user-attachments/assets/86bb29d6-5139-46d7-a95c-249b6c32cfa9" />

---

# Tech Stack

**Language**

Python

**Framework**

Streamlit

**Vector Database**

ChromaDB

**Embeddings**

SentenceTransformers

**LLM**

Google Gemini API

**Document Processing**

LangChain Document Loaders

---

# Key Features

• PDF document ingestion and processing
• Semantic search using vector embeddings
• Context-aware LLM responses
• Source citation from retrieved documents
• Modular RAG pipeline architecture
• Interactive Streamlit interface

---

# How It Works

## 1. Document Ingestion

PDF files are loaded and split into smaller chunks using a text splitter.
This improves retrieval accuracy by allowing the system to search smaller sections of documents.

## 2. Embedding Generation

Each text chunk is converted into vector embeddings using a **SentenceTransformer model**.

## 3. Vector Storage

The embeddings are stored in **ChromaDB**, enabling efficient similarity search.

## 4. Retrieval

When a user asks a question, the system retrieves the most relevant document chunks using vector similarity.

## 5. Answer Generation

The retrieved context is passed to the **Gemini LLM**, which generates the final answer based on the relevant document information.

---
<img width="659" height="310" alt="image" src="https://github.com/user-attachments/assets/fe35e0d3-8520-4a89-b224-b1dcdfdd5a7d" />

# Ouput/Example Query

<img width="949" height="468" alt="image" src="https://github.com/user-attachments/assets/1abc79c9-405e-45ca-abee-cf435e89b50b" />


# Installation

## Clone the repository

```
git clone https://github.com/Vaish-d30/RAG-Based-AI-Document-Assistant.git
cd RAG-Based-AI-Document-Assistant
```

## Install dependencies

```
pip install -r requirements.txt
```

## Add Gemini API key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

## Run the application

```
streamlit run app.py
```

---

# Future Improvements

• Multi-document knowledge base
• Conversational memory for chat interactions
• Hybrid search (vector + keyword retrieval)
• Document upload interface
• Cloud deployment for public access
• Support for additional document formats

---

# Author

Vaishnavi Desai
AI & Data Science Engineering Student

GitHub:
https://github.com/Vaish-d30
