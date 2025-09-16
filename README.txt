📖 RAGify Transcript: AI-Powered Video Q/A Assistant

RAGify Transcript is a Retrieval-Augmented Generation (RAG) system that enables intelligent, context-aware Q&A over transcripts. It combines semantic embeddings, vector search, and a lightweight LLM to deliver accurate and informative responses in real time, while politely rejecting off-topic queries.

🚀 Features

Upload and preprocess transcripts with text splitting.

Retrieve context using FAISS vector search + MiniLM-L6-v2 embeddings.

Generate answers with Flan-T5 Small via HuggingFace Transformers.

Apply prompt engineering for clarity and conciseness.

Relevance filtering ensures only transcript-related queries are answered.

Interactive deployment with Streamlit.

🏗️ Tech Stack

Programming: Python

Frameworks: LangChain, Streamlit

Models: Flan-T5 Small (LLM), MiniLM-L6-v2 (Embeddings)

Libraries: FAISS, HuggingFace Transformers, SentenceTransformers

Techniques: Semantic search, vector indexing, prompt engineering, text preprocessing, pipeline design

⚙️ Setup
git clone https://github.com/Abhi-it14/ragify-transcript.git
cd ragify-transcript
pip install -r requirements.txt
streamlit run app.py

📊 Highlights

Processed 50+ transcript chunks for contextual retrieval.

Achieved 85%+ accuracy on relevant answers during testing.

Delivered <1s query response times using FAISS indexing.

Optimized pipeline for modular integration and scalable Q&A flow.

🖼️ Architecture
flowchart TD
    A[Transcript Upload] --> B[Text Preprocessing & Chunking]
    B --> C[MiniLM-L6-v2 Embeddings]
    C --> D[FAISS Vector Store]
    D --> E[Semantic Search & Relevance Filtering]
    E --> F[Prompt Engineering]
    F --> G[Flan-T5 Small (LLM)]
    G --> H[Final Answer]

📌 Future Enhancements

Add support for YouTube transcripts and PDF parsing.

Integration with advanced LLMs (Flan-T5 XL, LLaMA 3, Mistral).

Cloud deployment for production-grade scalability.

⚡ RAGify Transcript combines retrieval, relevance, and generation for a professional-grade AI assistant experience.
