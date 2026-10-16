# RAGify Transcript
## AI-Powered Video Q&A Assistant

**RAGify Transcript** is a Retrieval-Augmented Generation (RAG) application that enables context-aware question answering over video transcripts. It combines semantic embeddings, FAISS vector search, and Flan-T5 Small to retrieve relevant information and generate concise, transcript-grounded responses.

---

## 🚀 Key Features

- **Transcript Processing** — Upload, preprocess, and split transcripts into manageable text chunks.
- **Semantic Search** — Retrieve relevant passages using MiniLM-L6-v2 embeddings and FAISS.
- **AI-Powered Answers** — Generate contextual responses using Flan-T5 Small.
- **Relevance Filtering** — Filter out questions unrelated to the transcript.
- **Prompt Engineering** — Improve response clarity and conciseness.
- **Interactive Interface** — Use the assistant through Streamlit.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Streamlit | User interface |
| LangChain | RAG pipeline integration |
| MiniLM-L6-v2 | Text embeddings |
| FAISS | Vector similarity search |
| Flan-T5 Small | Answer generation |
| HuggingFace Transformers | Model inference |
| SentenceTransformers | Embedding generation |

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[Transcript Upload] --> B[Text Preprocessing]
    B --> C[Text Chunking]
    C --> D[MiniLM Embeddings]
    D --> E[FAISS Vector Search]
    E --> F[Relevance Filtering]
    F --> G[Prompt Construction]
    G --> H[Flan-T5 Small]
    H --> I[Contextual Answer]
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/Abhi-it14/ragify-transcript.git
cd ragify-transcript
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Launch the application**

```bash
streamlit run app.py
```

Open the local URL provided in your terminal to start using the assistant.

## 📊 Project Highlights

- **50+ transcript chunks** processed for contextual retrieval.
- **85%+ reported answer accuracy** during testing.
- **Under 1 second reported query response time** with FAISS indexing.

*Reported figures should be interpreted in the context of the project's original testing setup.*

## 🔮 Future Enhancements

- YouTube transcript extraction and support for additional document formats.
- Integration with more advanced language models.
- Improved retrieval evaluation and answer-quality testing.
- Cloud deployment and scalability improvements.

---

## 🎯 Project Objective

Demonstrate how **Retrieval-Augmented Generation, semantic search, vector indexing, and language models** can work together to build a focused question-answering assistant over unstructured text.

**Core Skills:** Python · NLP · RAG · FAISS · HuggingFace · Semantic Search · Streamlit

**Repository:** [RAGify Transcript on GitHub](https://github.com/Abhi-it14/ragify-transcript)