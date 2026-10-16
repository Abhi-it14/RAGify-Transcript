# RAGify Transcript

Retrieval-Augmented Generation for Transcript-Based Question Answering

RAGify Transcript is a lightweight Python project that demonstrates a Retrieval-Augmented Generation (RAG) pipeline over video or audio transcripts. The project combines semantic retrieval (dense embeddings + FAISS) with prompt-driven generation to produce grounded answers from transcript content.

## Core Capabilities

- Text preprocessing and chunking for context preservation
- Dense embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- FAISS-based vector indexing and similarity search
- Context-aware generation (prompt + retrieved context) using Flan-T5 (HuggingFace)
- Query relevance filtering to reduce unsupported/off-topic answers
- Interactive Streamlit UI for transcript upload and Q&A

## Technical Stack

- Language: Python
- Web UI: Streamlit
- RAG orchestration: LangChain (optional integration)
- Embeddings: SentenceTransformers (MiniLM-L6-v2)
- Vector index: FAISS
- Generation model: Flan-T5 (small) via HuggingFace Transformers

## System Pipeline

1. Input processing: accept and clean transcript text
2. Chunking: split transcript into overlapping segments
3. Embedding: encode chunks using MiniLM-L6-v2
4. Indexing: store embeddings in FAISS
5. Query encoding: embed incoming question
6. Similarity search: retrieve top-K relevant chunks
7. Relevance validation: optionally filter/reject unrelated queries
8. Prompt construction: combine retrieved context + user question
9. Generation: produce an answer with Flan-T5
10. Response delivery: show the result in Streamlit

## Installation

Prerequisites:
- Python 3.8+
- Git

1. Clone this repository:

```bash
git clone https://github.com/Abhi-it14/RAGify-Transcript.git
cd RAGify-Transcript
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Note: model weights will be downloaded on first run (requires network access).

## Run the Streamlit App

Launch the interactive UI:

```bash
streamlit run rag_system_streamlit.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

## Usage Notes

- Supply a transcript (plain text) in the Streamlit interface or modify the script to load files programmatically.
- Adjust chunk size, overlap, and top-k retrieval settings inside the code if you need different retrieval behavior.
- If you want to use a different generation or embedding model, update the model names in the script and install any required packages.

## Reported Performance (informational)

- Answer accuracy (reported): ~85% (project note)
- Latency: depends on model size and hardware; small models typically respond in under a second for retrieval + encoding on modern CPUs, but generation may take longer.

These are illustrative figures — your results will vary by dataset, model, and hardware.

## Potential Extensions

- Add YouTube transcript ingestion
- Support multiple document formats (PDF, SRT, VTT)
- Experiment with larger embedding or generation models
- Add reranking or supervised fine-tuning for improved precision
- Add automated evaluation and benchmark scripts

---

