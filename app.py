import os
import streamlit as st

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Baahubali AI Chatbot")

st.title("🤖 Baahubali AI Chatbot (RAG)")

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# CLEAR CHAT
# -----------------------------
if st.button("🗑️ Clear Conversation"):
    st.session_state.messages = []
    st.rerun()

# -----------------------------
# READ FILES
# -----------------------------
def read_text_files(folder):
    text = ""

    if not os.path.exists(folder):
        return ""

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(
                os.path.join(folder, file),
                "r",
                encoding="utf-8"
            ) as f:
                text += f.read() + "\n"

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
@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# -----------------------------
# CREATE VECTOR DB
# -----------------------------
def create_vector_db(chunks):
    db = FAISS.from_texts(
        chunks,
        embedding=get_embeddings()
    )

    db.save_local("faiss_index")

# -----------------------------
# LOAD LLM
# -----------------------------
@st.cache_resource
def get_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

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

        st.success(
            f"Data processed successfully! {len(chunks)} chunks created."
        )

# -----------------------------
# SHOW CHAT HISTORY
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------
question = st.chat_input(
    "Ask anything about Baahubali..."
)

if question:

    if not os.path.exists("faiss_index"):
        st.warning(
            "⚠️ Please click 'Process Story Files' first."
        )
        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    db = FAISS.load_local(
        "faiss_index",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    llm = get_llm()

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

If the answer is not found in the context,
say:
"I don't know based on the document."
"""

    response = llm.invoke(prompt)

    answer = response.content

    with st.chat_message("assistant"):
        st.markdown(answer)

        with st.expander("📄 Retrieved Chunks Used"):
            st.write(context)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )