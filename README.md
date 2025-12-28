# 🚀 DocMind ChatBot

**Intelligent Local Document Intelligence Engine**

**DocMind** is a powerful, fully offline Retrieval-Augmented Generation (RAG) application that enables natural language interaction with your documents. Upload PDFs, images, spreadsheets, or text files — ask complex questions — receive accurate, context-aware answers with full source transparency.

All processing happens locally on your machine. No data leaves your device. No API costs. Complete privacy.

## 🌟 Core Capabilities

- **Wide Document Compatibility**  
  PDF • DOCX • TXT • CSV • JSON • Excel • Images (JPG, PNG, BMP, TIFF)

- **High-Accuracy OCR**  
  Powered by **easyOCR** – multilingual support (English + Bengali), superior performance on scanned documents and photos

- **Advanced RAG Pipeline**  
  - Semantic chunking with overlap (`RecursiveCharacterTextSplitter`)
  - State-of-the-art embeddings using **nomic-embed-text** (MTEB leaderboard top-tier)
  - Persistent **FAISS** vector store with incremental merging (multi-document knowledge retention)
  - Rich metadata: filename, page number, chunk preview

- **Intelligent Query Processing**  
  - Precise answers from text documents
  - Full support for image-based questions (headlines, summaries, diagrams, charts)
  - Smart text extraction commands ("extract text", "read text from image")
  - Expandable source references for every answer

- **100% Local Execution**  
  - LLM: **llama3.2:3b** via Ollama
  - Embeddings: **nomic-embed-text** via Ollama
  - Zero external dependencies • No internet required after setup • Unlimited usage

- **Production-Grade Architecture**  
  - FastAPI backend (clean REST endpoints, Pydantic validation)
  - Modern Streamlit frontend (drag-and-drop, real-time chat)
  - Docker support for reproducible deployment

## 🛠️ Technology Stack

| Component       | Technology                        | Advantage                          |
|-----------------|-----------------------------------|------------------------------------|
| Backend         | FastAPI                           | High performance, automatic docs   |
| RAG Framework   | LangChain                         | Robust retrieval and chaining      |
| Vector Store    | FAISS (incremental merge)         | Fast, persistent, local            |
| Embeddings      | nomic-embed-text (Ollama)         | SOTA open-source quality           |
| LLM             | llama3.2:3b (Ollama)              | Strong reasoning, fully local      |
| OCR             | easyOCR                           | Multilingual, high accuracy        |
| Frontend        | Streamlit                         | Interactive, rapid development     |
| Deployment      | Docker                            | Consistent environment             |

## 🚀 Quick Start

### Prerequisites
```bash
# Install Ollama<a href="https://ollama.com" target="_blank" rel="noopener noreferrer nofollow"></a>
ollama pull llama3.2:3b
ollama pull nomic-embed-text
Setup & Run
Bash# Clone and install
git clone https://github.com/yourusername/DocMind-ChatBot.git
cd DocMind-ChatBot
pip install -r requirements.txt

# Run backend
uvicorn main:app --reload
# API docs: http://localhost:8000/docs

# Run frontend (new terminal)
streamlit run streamlit_app.py
# Open http://localhost:8501
Docker Deployment
Bashdocker build -t docmind .
docker run -p 8501:8501 docmind
🔌 API Usage
POST /upload
Upload and index documents
JSONfiles: { "file": (filename, file_data) }
POST /query
Ask questions
JSON{
  "question": "What are the payment terms in the invoice?",
  "image_base64": "optional_base64_string"  // for direct image query
}
Response includes:
JSON{
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

⚙️ Environment Setup
Create .env from template:
env# .env.example
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
OLLAMA_LLM_MODEL=llama3.2:3b
The application automatically loads these on startup.


📸 Experience Highlights

Drag-and-drop multiple documents
Real-time chat with source citations
Seamless handling of mixed content (PDFs + images)
Persistent knowledge across sessions

🔒 Privacy & Performance

Complete Data Privacy — Nothing leaves your machine
Zero Ongoing Cost — No tokens, no subscriptions
High Accuracy — Context-only prompting minimizes hallucinations
Fast Response — Local inference with optimized retrieval

🙏 Built With
LangChain • Ollama • FAISS • easyOCR • FastAPI • Streamlit
DocMind — Your documents, intelligently understood.
Crafted by [Md Masud Rana]
