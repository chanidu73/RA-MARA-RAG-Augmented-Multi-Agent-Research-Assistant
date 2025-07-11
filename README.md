#  RAG-Based Multi-Agent Research Assistant

This is a lightweight Retrieval-Augmented Generation (RAG) assistant that leverages LangChain, Hugging Face Transformers, and FAISS for efficient document-based question answering.

---

## Features

-  Vector search over your context documents using FAISS
-  Lightweight language model for generation (`falcon-rw-1b`, `meta-llama/Llama-3.2-1B`)
-  RetrievalQA pipeline using LangChain
-  Works well on CPU-based systems (Use `falcon-rw-1b`)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/chanidu73/RA-MARA-RAG-Augmented-Multi-Agent-Research-Assistan.git
cd RAG-Based-Multi-Agent-Research-Assistant-RA-MARA/ra-mara
