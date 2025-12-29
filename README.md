#  DocMind ChatBot

**Smart Local RAG Document Chatbot with OCR Support**

**DocMind** is a fully local and private Retrieval-Augmented Generation (RAG) document chatbot built using FastAPI, LangChain, FAISS, and Ollama. It allows users to upload various document types (PDF, DOCX, TXT, CSV, JSON, Excel, images) and ask natural language questions, receiving accurate answers with source references -all running offline using Ollama

# Key Highlights
  - Supports PDF, Word files, spreadsheets, and images with high-accuracy OCR (easyOCR)
  - Uses nomic-embed-text embeddings and FAISS vector store with metadata tracking
  - Smart handling of both text and image-based questions
  - Answers include expandable source citations (filename, page, preview)
  - Powered by Ollama (llama3.2:3b) – completely offline, zero cost, full data privacy
  - Professional Streamlit UI with drag-and-drop upload and chat interface
  - Docker-ready for easy deployment

##  Key Features

- **Multi-Format Document Support**  
  PDF • DOCX • TXT • CSV • JSON • Excel (.xlsx) • Images (JPG, PNG, BMP, TIFF)

- **Advanced OCR for Images**  
  Powered by **easyOCR** – high accuracy with multilingual support (English + Bengali)

- **Intelligent RAG Pipeline**  
  - Text chunking with overlap using `RecursiveCharacterTextSplitter`
  - State-of-the-art local embeddings with **nomic-embed-text** (comparable to or better than OpenAI models)
  - Persistent FAISS vector store with incremental merging for multi-document sessions
  - Rich metadata tracking: filename, page number, chunk preview

- **Smart Query Handling**  
  - General questions from text documents
  - Image-based questions (headlines, summaries, diagrams, charts)
  - Direct text extraction commands ("extract text", "read text from image")
  - Answers include **expandable source references** for full transparency

- **100% Local & Private**  
  Powered by **Ollama**  
  - LLM: llama3.2:3b  
  - Embeddings: nomic-embed-text  
  No external APIs • Zero cost • Complete data privacy

- **Professional Architecture**  
  - FastAPI backend with clean endpoints and Pydantic validation
  - Streamlit frontend with drag-and-drop upload and modern chat interface
  - Docker-ready for reproducible deployment

##  Technology Stack

| Component       | Technology                          |
|-----------------|-------------------------------------|
| Backend         | FastAPI                             |
| RAG Framework   | LangChain                           |
| Vector Store    | FAISS (incremental merge)           |
| Embeddings      | nomic-embed-text (Ollama)           |
| LLM             | llama3.2:3b (Ollama)                |
| OCR             | easyOCR                             |
| Frontend        | Streamlit                           |
| Deployment      | Docker                              |

##  Quick Start

### Prerequisites
```bash
# Install Ollama from https://ollama.com
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

### Setup & Run
```Bash
# Clone the repository
git clone https://github.com/masud770/DocMind-ChatBot.git
cd DocMind-ChatBot

# Install dependencies
pip install -r requirements.txt

# Run the backend
uvicorn main:app --reload
# API docs available at http://localhost:8000/docs

# Run the frontend (in a new terminal)
streamlit run streamlit_app.py
# Open http://localhost:8501 in your browser
```
## Docker Deployment
```Bash
docker build -t docmind.
docker run -p 8501:8501 docmind
```

##  How to Use DocMind

  1. **Upload Documents**  
     Drag-and-drop files in the sidebar (supports PDF, images, Word, Excel, etc.)
  
  2. **Ask Questions**  
     Type your question in the chat box (e.g., "What is the objective?", "Extract text from image")
  
  3. **View Sources**  
     Click "View Sources" expander to see filename, page, and preview
  
  4. **Multi-Document Query**  
     Upload multiple files — ask questions across all of them
  
  5. **Image Questions**  
     Ask "extract text", "summarize news in image", "what is the headline"
## 🔌 API Usage

POST /upload – Upload and index documents
  - Form Data: file (binary file)
  - POST /query – Ask questions
  
Request Body (JSON):
```JSON
{
  "question": "What are the payment terms in the invoice?",
  "image_base64": "optional_base64_encoded_image"  // For direct image query
}
```
Response:
```JSON
{
  "answer": "Payment is due within 30 days.",
  "sources": [
    {
      "file": "invoice.pdf",
      "page": "1",
      "preview": "Payment due within 30 days from..."
    }
  ]
}
```
# Additional Endpoints

    - GET / - Welcome message
    - GET /health - System status
    - POST /clear - Reset vector store

Interactive API documentation: http://localhost:8000/docs (Swagger UI)

##  Environment Setup
Create a .env file from the template:
```env
# .env.example
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
OLLAMA_LLM_MODEL=llama3.2:3b
```
##  Experience Highlights

  - Drag-and-drop multiple document upload
  - Real-time conversational interface
  - Mixed content handling (PDF + images in the same session)
  - Persistent knowledge across restarts
  - Source citations for every answer

##  Privacy & Performance

Complete Data Privacy - No data leaves your machine
Zero Cost - No tokens or subscriptions
High Accuracy - Strict context-only prompting reduces hallucinations
Fast Local Inference - Optimized retrieval and response times

##  Built With
  - LangChain • Ollama • FAISS • easyOCR • FastAPI • Streamlit
  - DocMind - Your documents, intelligently understood. Privately. Locally.
# **Crafted by [Md Masud Rana](https://www.linkedin.com/in/masudr760/)** 




