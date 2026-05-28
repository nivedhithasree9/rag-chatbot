import os
import streamlit as st

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# -----------------------------
# API KEY (PASTE YOUR GROQ KEY)
# -----------------------------
GROQ_API_KEY = "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"

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Baahubali AI Chatbot")

st.title("🤖 Baahubali AI Chatbot (REAL AI + RAG)")

# -----------------------------
# READ FILES
# -----------------------------
def read_text_files(folder):
    text = ""
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                text += f.read()
    return text

# -----------------------------
# SPLIT TEXT
# -----------------------------
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_text(text)

# -----------------------------
# EMBEDDINGS
# -----------------------------
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# -----------------------------
# CREATE VECTOR DB
# -----------------------------
def create_vector_db(chunks):
    db = FAISS.from_texts(chunks, embedding=get_embeddings())
    db.save_local("faiss_index")

# -----------------------------
# LOAD AI MODEL (REAL AI)
# -----------------------------
def get_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

# -----------------------------
# ASK QUESTION
# -----------------------------
def ask_question(question):

    db = FAISS.load_local(
        "faiss_index",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(question)

    context = "\n".join([d.page_content for d in docs])

    llm = get_llm()

    # STEP 1: CHECK IF RELATED TO STORY
    check_prompt = f"""
Answer ONLY YES or NO.

Question: {question}

Context: {context}

Is this question related to Baahubali story?
"""

    check = llm.invoke(check_prompt).content.lower()

    if "no" in check:
        st.warning("❌ This is not related to Baahubali story.\n👉 Ask only story-related questions.")
        return

    # STEP 2: FINAL ANSWER
    prompt = f"""
You are a helpful AI assistant.

Use the context to answer the question.

Context:
{context}

Question:
{question}

If answer is not in context, say you don't know.
"""

    response = llm.invoke(prompt)

    st.subheader("🤖 Answer")
    st.write(response.content)

# -----------------------------
# PROCESS FILES
# -----------------------------
if st.button("📂 Process Story Files"):

    raw_text = read_text_files("data")

    if not raw_text.strip():
        st.error("No text found in data folder!")
    else:
        chunks = split_text(raw_text)
        create_vector_db(chunks)
        st.success("Data processed successfully!")

# -----------------------------
# USER INPUT
# -----------------------------
question = st.text_input("Ask anything about Baahubali")

if question:
    ask_question(question)