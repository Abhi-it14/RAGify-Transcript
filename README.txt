# RAGify Transcript

## Retrieval-Augmented Generation for Transcript-Based Question Answering

RAGify Transcript is a Python-based question-answering system that implements a Retrieval-Augmented Generation (RAG) pipeline over video transcripts. It combines dense vector embeddings, FAISS-based similarity search, context retrieval, and transformer-based text generation to produce context-aware answers grounded in transcript content.

The system integrates semantic retrieval with prompt construction and relevance filtering to reduce off-topic responses and improve the relevance of generated answers.

---

# CORE CAPABILITIES

### 01. Text Preprocessing and Chunking
Processes transcript text and segments it into smaller chunks to support efficient embedding generation and context retrieval.

### 02. Dense Vector Embeddings
Uses the `sentence-transformers/all-MiniLM-L6-v2` embedding model to encode transcript chunks into dense vector representations for semantic similarity search.

### 03. Vector Indexing and Retrieval
Uses FAISS to index embeddings and retrieve transcript segments relevant to a user's query.

### 04. Context-Aware Generation
Passes retrieved transcript context and the user query into a prompt-driven generation pipeline powered by Flan-T5 Small.

### 05. Query Relevance Filtering
Applies relevance checks to help prevent unrelated questions from receiving unsupported transcript-based answers.

### 06. Interactive Inference Interface
Provides a Streamlit interface for transcript input and interactive question answering.

---

# TECHNICAL STACK

| Component | Implementation |
|---|---|
| Programming Language | Python |
| Application Layer | Streamlit |
| RAG Orchestration | LangChain |
| Embedding Model | MiniLM-L6-v2 |
| Vector Index | FAISS |
| Generative Model | Flan-T5 Small |
| Model Inference | HuggingFace Transformers |
| Embedding Utilities | SentenceTransformers |

---

# SYSTEM PIPELINE

The application follows a retrieval-first architecture in which transcript context is retrieved before answer generation.

1. **Input Processing:** Accept and preprocess transcript text.
2. **Chunking:** Split the transcript into smaller segments suitable for embedding and retrieval.
3. **Embedding Generation:** Encode each chunk into a dense vector representation using MiniLM-L6-v2.
4. **Index Construction:** Store the chunk embeddings in a FAISS vector index.
5. **Query Encoding:** Convert the incoming question into an embedding in the same vector space.
6. **Similarity Search:** Retrieve the most relevant transcript chunks using vector similarity.
7. **Relevance Validation:** Filter or reject queries that do not meet the application's relevance criteria.
8. **Prompt Construction:** Combine the query with the retrieved context.
9. **Text Generation:** Generate an answer using Flan-T5 Small through HuggingFace Transformers.
10. **Response Delivery:** Return the generated answer through the Streamlit interface.

---

# INSTALLATION AND EXECUTION

### Prerequisites

- Python
- Git
- Dependencies listed in `requirements.txt`
- Network access for downloading model artifacts when they are not cached locally

### 1. Clone the Repository

```bash
git clone https://github.com/Abhi-it14/ragify-transcript.git
cd ragify-transcript
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Application

```bash
streamlit run app.py
```

Streamlit will display a local URL where the application can be accessed.

---

# REPORTED PERFORMANCE

The original project notes report the following preliminary results:

| Evaluation Metric | Reported Result |
|---|---|
| Transcript chunks processed | 50+ |
| Answer accuracy | 85%+ |
| Query response time | Under 1 second |

These figures are reported project results, not independently validated benchmarks. Reproducibility depends on the evaluation dataset, hardware, model initialization, retrieval configuration, and timing methodology.

A more rigorous evaluation would measure retrieval precision, recall, answer correctness, response latency, and the rate of unsupported answers using a defined test set.

---

# ENGINEERING CONSIDERATIONS

- **Retrieval Quality:** Chunk size, overlap, embedding quality, and the number of retrieved passages influence context relevance.
- **Generation Grounding:** Answer quality depends on the relevance and completeness of the retrieved context and the generation prompt.
- **Relevance Thresholds:** Query filtering should be evaluated to balance off-topic rejection against valid-question coverage.
- **Latency:** End-to-end response time includes query embedding, vector search, prompt construction, and model inference.
- **Extensibility:** The retrieval and generation components can be evaluated and improved independently within the pipeline.

---

# POTENTIAL EXTENSIONS

- Add YouTube transcript ingestion and support for additional document formats.
- Experiment with alternative embedding models and retrieval configurations.
- Evaluate reranking methods for improving retrieved-context relevance.
- Explore larger language models, including LLaMA and Mistral.
- Introduce automated evaluation for retrieval quality and grounded answer generation.
- Optimize model loading, inference latency, and deployment for larger workloads.

---

# PROJECT OBJECTIVE

RAGify Transcript demonstrates the implementation of a retrieval-augmented question-answering workflow that connects text preprocessing, dense vector representations, approximate nearest-neighbor search, prompt construction, and transformer-based generation.

**Technical Focus:** Retrieval-Augmented Generation · NLP · Dense Embeddings · Vector Search · FAISS · LangChain · HuggingFace Transformers · Prompt Engineering · Streamlit

**Repository:** [Abhi-it14/ragify-transcript](https://github.com/Abhi-it14/ragify-transcript)