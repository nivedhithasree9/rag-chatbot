# 📚 Baahubali RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions about the Baahubali story using Streamlit, LangChain, FAISS, Sentence Transformers, and Groq LLM.

---

## 🚀 Features

- 📄 Document Processing
- ✂️ Automatic Text Chunking
- 🧠 Embedding Generation
- 🔎 FAISS Vector Search
- 💬 Chat-based Interface
- 📚 Retrieved Context Display
- 🗑️ Clear Conversation Option
- ⚡ Fast AI Responses

---

## 📊 What document did you use and why?

The chatbot uses the following documents:

- `bahubali_part1.txt`
- `bahubali_part2.txt`

These files contain the complete story of Baahubali Part 1 and Part 2. They were selected because they provide a structured knowledge base suitable for Retrieval-Augmented Generation (RAG).

---

## ✂️ How does your chunking work?

The project uses LangChain's `RecursiveCharacterTextSplitter`.

Configuration:

- Chunk Size: 500 characters
- Chunk Overlap: 100 characters

Chunking divides large documents into smaller meaningful sections while preserving context between chunks using overlap. This improves retrieval quality and answer accuracy.

---

## 🧠 Which embedding model did you use?

Embedding Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

This model converts text chunks into vector embeddings which are stored in FAISS and used for semantic similarity search.

---

## 🔎 Vector Store

The project uses **FAISS (Facebook AI Similarity Search)** as the vector database.

FAISS stores embeddings and retrieves the most relevant chunks based on the user's question.

---

## 🤖 LLM Used

- Groq API
- Llama 3.1 8B Instant

The retrieved document chunks are passed to the LLM as context to generate accurate answers.

---

## 📁 Project Structure

```text
rag-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── secrets.toml
├── data/
│   ├── bahubali_part1.txt
│   └── bahubali_part2.txt
└── faiss_index/
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/nivedhithasree9/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY="your_groq_api_key"
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshot

Add a screenshot of the running application.

```md
![App Screenshot](screenshot.png)
```

---

## 🔧 What would you improve with more time?

- Support multiple PDF uploads
- Add source citations
- Improve retrieval accuracy with reranking
- Add conversational memory
- Support multilingual documents
- Deploy with authentication

---

## 🛠️ Technologies Used

- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- Groq API
- Llama 3.1
- Python

---

## 👨‍💻 Author

Developed as a Retrieval-Augmented Generation (RAG) project using Streamlit and LangChain.