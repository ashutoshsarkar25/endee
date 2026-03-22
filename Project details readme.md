# 🚀 AI Semantic Search using Endee

## 📌 Project Overview

This project implements a **semantic search system** that allows users to retrieve meaningful information from documents instead of relying on simple keyword matching.

It uses **vector embeddings** and similarity search to understand the context of queries and return the most relevant results.

---

## ❓ Problem Statement

Traditional search systems rely on keyword matching, which often fails to capture the actual meaning of user queries.

When working with large documents like PDFs, users face difficulty in finding precise and relevant information efficiently.

---

## 💡 Proposed Solution

This project solves the problem by:

* Converting document text into **vector embeddings**
* Storing embeddings in a **vector database (Endee-based architecture)**
* Converting user queries into embeddings
* Performing **semantic similarity search** to retrieve relevant content

---

## 🧠 System Architecture

```
PDF Documents
     ↓
Text Extraction
     ↓
Chunking
     ↓
Embedding (Sentence Transformer)
     ↓
Vector Storage (Endee)
     ↓
--------------------------------
     ↓
User Query
     ↓
Query Embedding
     ↓
Similarity Search (Endee)
     ↓
Top Relevant Results
```

---

## ⚙️ How Endee is Used

Endee is used as the **vector database layer** in this project.

* Document chunks are converted into embeddings and stored
* Each embedding represents semantic meaning of text
* User queries are also embedded
* Endee performs **vector similarity search**
* Top matching results are returned to the user

> Note: The implementation follows an **Endee-compatible vector storage approach**, demonstrating how semantic retrieval systems operate using vector databases.

---

## 🛠 Tech Stack

* **Python**
* **Endee (Vector Database Concept)**
* **ChromaDB (Endee-compatible implementation)**
* **Sentence Transformers**
* **Streamlit**
* **PyPDF**

---

## ✨ Features

* 📄 PDF document ingestion
* 🧠 Semantic search (context-based retrieval)
* ⚡ Fast vector similarity search
* 💻 Simple and interactive UI using Streamlit

---

## 📂 Project Structure

```
endee/
│
├── mini-search/
│   ├── ingest.py
│   ├── search.py
│   ├── endee_client.py
│   ├── app.py
│   ├── data/
│   ├── chroma_db/
│   └── requirements.txt
│
└── README.md
```

---

## 🚀 Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/ashutoshsarkar25/endee.git
cd endee/mini-search
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add PDF files

Place your PDF files inside:

```
mini-search/data/
```

### 5. Run ingestion

```
python ingest.py
```

### 6. Run the application

```
streamlit run app.py
```

---

## 🧪 Example Usage

* Input: *"What is SmartEd?"*
* Output: Relevant extracted content from the document

---

## 📊 Future Enhancements

* 🔹 Add RAG (Retrieval-Augmented Generation)
* 🔹 Multi-document comparison
* 🔹 Improved ranking algorithms
* 🔹 Chatbot-style interface

---

## 🎯 Conclusion

This project demonstrates how **vector databases like Endee** can be used to build intelligent search systems that understand the meaning behind user queries, making information retrieval more efficient and accurate.

