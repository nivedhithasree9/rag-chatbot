# 📚 Baahubali RAG Chatbot (Streamlit + Gemini AI)

A simple **Retrieval-Augmented Generation (RAG)** project that answers questions based on Baahubali Part 1 and Part 2 story data using Streamlit, LangChain, FAISS, and Google Gemini AI.

---

## 🚀 Features

- 📄 Loads story from `.txt` files
- 🧠 Uses Google Gemini 1.5 Flash model
- 🔎 FAISS vector search for similarity matching
- 💬 Ask questions in natural language
- ⚡ Simple Streamlit web interface

---

## 📁 Project Structure
-  rag_project/
        ├── app.py
        ├── requirements.txt
        ├── README.md
        ├── .gitignore
        └── data/
                ├── bahubali_part1.txt
                ├── bahubali_part2.txt

                ---

## 📊 Dataset

All data is stored in the `data/` folder:

- `bahubali_part1.txt` → Baahubali: The Beginning story
- `bahubali_part2.txt` → Baahubali: The Conclusion story

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://code.swecha.org/Nivedhitha/rag_project.git
cd rag_project