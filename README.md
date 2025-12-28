# 🚀 DocMind ChatBot

**Smart Local RAG Document Chatbot with OCR Support**

**DocMind** is a fully local, private, and intelligent Retrieval-Augmented Generation (RAG) document chatbot. It enables natural language querying over uploaded documents (PDF, images, Word files, spreadsheets) with accurate answers and source references — all running offline using Ollama.

## 🌟 Key Features

- **Multi-Format Document Support**
  PDF • DOCX • TXT • CSV • JSON • Excel • Images

- **Advanced OCR**  
  Powered by **easyOCR** – high accuracy, multilingual (English + Bengali)

- **Intelligent RAG Pipeline**  
  - Text chunking with overlap (`RecursiveCharacterTextSplitter`)
  - Embeddings: **nomic-embed-text** (state-of-the-art open-source)
  - Persistent FAISS vector store with incremental merging
  - Rich metadata tracking (filename, page, chunk preview)

- **Smart Query Handling**  
  - General questions from text documents
  - Image-based questions (headlines, summaries, diagrams)
  - Direct text extraction ("extract text", "read text from image")
  - Answers include **expandable source references**

- **100% Local & Private**  
  Powered by **Ollama** (llama3.2:3b + nomic-embed-text)  
  No external APIs • Zero cost • Complete data privacy

- **Professional Architecture**  
  - FastAPI backend
  - Streamlit frontend (drag-and-drop + chat interface)
  - Docker-ready

## 🛠️ Technology Stack

| Component       | Technology                          |
|-----------------|-------------------------------------|
| Backend         | FastAPI                             |
| RAG Framework   | LangChain                           |
| Vector Store    | FAISS (incremental)                 |
| Embeddings      | nomic-embed-text (Ollama)           |
| LLM             | llama3.2:3b (Ollama)                |
| OCR             | easyOCR                             |
| Frontend        | Streamlit                           |
| Deployment      | Docker                              |

## 🚀 Quick Start

### Prerequisites
```bash
# Install Ollama<a href="https://ollama.com" target="_blank" rel="noopener noreferrer nofollow"></a>
ollama pull llama3.2:3b
ollama pull nomic-embed-text

### Setup & Run

```bash
# Clone and install
git clone https://github.com/masud770/DocMind-ChatBot.git
cd DocMind-ChatBot
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload
# API docs: http://localhost:8000/docs

# Run frontend (new terminal)
streamlit run streamlit_app.py
# Open http://localhost:8501

###Docker Deployment

Bashdocker build -t docmind .
docker run -p 8501:8501 docmind

###🔌 API Usage
POST /upload
Upload and index documents

files: { "file": (filename, file_data) }

POST /query
Ask questions

files: { "file": (filename, file_data) }

Response includes:
{
  "answer": "Payment due within 30 days...",
  "sources": [
    {
      "file": "invoice.pdf",
      "page": "1",
      "preview": "Payment due within 30 days from..."
    }
  ]
}
Additional Endpoints

GET /health → System status
POST /clear → Reset knowledge base

### ⚙️ Environment Setup
Create .env from template:

# .env.example
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
OLLAMA_LLM_MODEL=llama3.2:3b


### 📸 Experience Highlights

Drag-and-drop multiple documents
Real-time chat with source citations
Seamless handling of mixed content (PDFs + images)
Persistent knowledge across sessions

### 🔒 Privacy & Performance

Complete Data Privacy — Nothing leaves your machine
Zero Ongoing Cost — No tokens, no subscriptions
High Accuracy — Context-only prompting minimizes hallucinations
Fast Response — Local inference with optimized retrieval

### 🙏 Built With
LangChain • Ollama • FAISS • easyOCR • FastAPI • Streamlit
DocMind — Your documents, intelligently understood.
Crafted by [Md Masud Rana]
