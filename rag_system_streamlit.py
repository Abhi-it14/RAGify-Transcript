# -----------------------------
# rag_system_streamlit.py
# -----------------------------
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

st.set_page_config(page_title="🎥 YouTube Transcript Q&A", layout="wide")
st.title("🎥 Transcript Q&A System (Free)")

# -----------------------------
# Step 1: Upload transcript
# -----------------------------
uploaded_file = st.file_uploader("Upload transcript (.txt)", type="txt")

if uploaded_file is None:
    st.warning("Please upload a transcript file to proceed.")
    st.stop()

transcript_text = uploaded_file.read().decode("utf-8")

# -----------------------------
# Step 2: Split transcript into chunks
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
chunks = text_splitter.split_text(transcript_text)
st.success(f"Transcript split into {len(chunks)} chunks.")

# -----------------------------
# Step 3: Create embeddings (Free)
# -----------------------------
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
faiss_index = FAISS.from_texts(chunks, embedding_model)
st.success("FAISS index created successfully.")

# -----------------------------
# Step 4: Load free local LLM (Flan-T5 Small)
# -----------------------------
qa_model = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    tokenizer="google/flan-t5-small",
    device=-1  # CPU
)

# -----------------------------
# Step 5: Q&A interface
# -----------------------------
st.subheader("Ask a question about the transcript:")

query = st.text_input("Your question")
if query:
    # Retrieve top 3 relevant chunks
    docs = faiss_index.similarity_search(query, k=3)
    if not docs:
        st.markdown("📌 Answer: This topic is not covered in the video.")
    else:
        # Combine and limit context
        context_text = " ".join([doc.page_content.strip() for doc in docs])
        context_text = context_text[:1500]

        # Prompt for LLM
        prompt = f"""
        You are an expert AI assistant. Answer the question ONLY using the context below.
        Context: {context_text}
        Question: {query}
        If the answer is not in the context, respond: "This topic is not covered in the video."
        Answer politely and concisely.
        """

        # Generate answer
        result = qa_model(prompt, max_new_tokens=150, do_sample=False)[0]['generated_text']
        st.markdown(f"📌 Answer: {result}")


