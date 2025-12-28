# DocMind-ChatBot
**Generative AI & Chatbot Development - Python Assignment**
**DocMind** is a production-quality, fully offline RAG application that turns any document into an intelligent conversational assistant. It supports a wide range of document formats, performs accurate OCR on images, and provides answers with transparent source references — all while keeping your data 100% private.

## 🌟 Key Features

- **Multi-Format Document Support**  
  PDF, DOCX, TXT, CSV, JSON, Excel (.xlsx), Images (JPG, PNG, BMP, TIFF)

- **Advanced OCR for Images**  
  Powered by **easyOCR** (superior accuracy, supports English + Bengali)

- **Intelligent RAG Pipeline**  
  - Text chunking with overlap using `RecursiveCharacterTextSplitter`
  - State-of-the-art local embeddings with **nomic-embed-text** (comparable to or better than OpenAI's text-embedding-3-small)
  - Persistent FAISS vector store with incremental merging for multi-document sessions
  - Rich metadata tracking: filename, page number, chunk preview

- **Smart Query Handling**  
  - General questions from PDFs, Word files, etc.
  - Image-based questions (headlines, summaries, diagrams, etc.)
  - Direct text extraction commands ("extract text", "read text from image")
  - Answers include expandable **source references** for full transparency

- **Local & Private LLM**  
  Powered by **Ollama + llama3.2:3b** — completely offline, zero cost, full data privacy

- **Professional Architecture**  
  - FastAPI backend with clean endpoints and Pydantic models
  - Streamlit frontend with drag-and-drop upload and chat-style interface
  - Docker-ready for easy deployment

- **Bonus Features Implemented**
  - Multi-document support
  - Source citation in responses
  - Enhanced handling of image-based questions
  - Fully local execution (no external APIs or keys required)

## 🛠️ Technology Stack

| Component              | Technology Used                          | Reason |
|------------------------|------------------------------------------|--------|
| Backend                | FastAPI                                  | High performance, async support, automatic docs |
| RAG Framework          | LangChain                                | Streamlined retrieval and chaining |
| Vector Store           | FAISS (with incremental merge)           | Fast similarity search, local persistence |
| Embeddings             | nomic-embed-text (via Ollama)            | State-of-the-art open-source embeddings, private |
| LLM                    | llama3.2:3b (via Ollama)                 | Strong reasoning, fully local |
| OCR                    | easyOCR                                  | Better accuracy than pytesseract, multilingual |
| Frontend               | Streamlit                                | Rapid, clean, interactive UI |
| Containerization       | Docker                                   | Easy deployment and reproducibility |

## 🚀 Quick Start

```bash
# 1. Install Ollama and pull models
ollama pull llama3.2:3b
ollama pull nomic-embed-text

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the API
uvicorn main:app --reload

# 4. Run the UI (in a new terminal)
streamlit run streamlit_app.py
