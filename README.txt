# RAGify Transcript — AI-Powered Video Q&A Assistant

RAGify Transcript is a Retrieval-Augmented Generation (RAG) application that enables context-aware question answering over video transcripts. It combines semantic embeddings, FAISS vector search, and a lightweight language model to retrieve relevant information and generate concise, transcript-grounded responses.

The application also filters off-topic queries to keep responses relevant to the uploaded content.

## Key Features

- **Transcript Processing:** Upload, preprocess, and split transcripts into manageable text chunks.
- **Semantic Retrieval:** Retrieve relevant context using FAISS vector search and MiniLM-L6-v2 embeddings.
- **Contextual Answer Generation:** Generate responses using Flan-T5 Small through HuggingFace Transformers.
- **Relevance Filtering:** Restrict responses to questions related to the transcript content.
- **Prompt Engineering:** Structure prompts to improve answer clarity and conciseness.
- **Interactive Interface:** Access the assistant through a Streamlit application.

## Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Application Framework | Streamlit |
| RAG Framework | LangChain |
| Embedding Model | MiniLM-L6-v2 |
| Language Model | Flan-T5 Small |
| Vector Search | FAISS |
| NLP Libraries | HuggingFace Transformers, SentenceTransformers |

## System Architecture

The application follows a retrieval-and-generation pipeline:

```mermaid
flowchart TD
    A[Transcript Upload] --> B[Text Preprocessing & Chunking]
    B --> C[MiniLM-L6-v2 Embeddings]
    C --> D[FAISS Vector Index]
    D --> E[Semantic Retrieval]
    E --> F[Relevance Filtering]
    F --> G[Prompt Construction]
    G --> H[Flan-T5 Small]
    H --> I[Contextual Answer]
```

## Getting Started

### Prerequisites

- Python installed
- Git
- Access to the required model files or the ability to download them

### Installation

Clone the repository:

```bash
git clone https://github.com/Abhi-it14/ragify-transcript.git
cd ragify-transcript
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to interact with the assistant.

## Implementation Highlights

- Processes transcripts into chunks suitable for semantic retrieval.
- Uses dense embeddings to identify contextually relevant transcript passages.
- Integrates vector search with language-model generation in a single pipeline.
- Applies relevance filtering to reduce responses to unrelated queries.
- Uses a modular workflow that can be extended with additional transcript sources and language models.

### Reported Testing Results

The original project notes report the following results:

- **50+ transcript chunks** processed for contextual retrieval.
- **85%+ answer accuracy** during testing.
- **Under one second** query response time with FAISS indexing.

These figures are reported project results; reproducibility depends on the evaluation dataset, hardware, retrieval configuration, and measurement methodology.

## Future Enhancements

- Support for YouTube transcript extraction and additional document formats.
- Integration with more capable language models, including LLaMA and Mistral.
- Improved retrieval evaluation and answer-quality testing.
- Cloud deployment and performance optimization for larger workloads.

## Project Objective

RAGify Transcript demonstrates how semantic search, vector indexing, and language-model generation can be combined to build a focused question-answering assistant over unstructured text.

**Core capabilities:** Retrieval-Augmented Generation · Semantic Search · NLP · Vector Databases · Prompt Engineering · Streamlit

---

**Repository:** [Abhi-it14/ragify-transcript](https://github.com/Abhi-it14/ragify-transcript)
