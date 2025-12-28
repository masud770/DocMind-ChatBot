import os
import uuid
import shutil
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from models import UploadResponse, QueryRequest, QueryResponse
from utils import get_document_loader, split_docs, ocr_from_base64
from rag import add_document_to_vectorstore, get_qa_chain
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = "uploads"
VECTORSTORE_DIR = "vectorstore"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTORSTORE_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Smart RAG Document Chatbot",
    description="Local RAG API - No API Key Needed | Ollama Llama3.2:3b",
    version="Final Local Version"
)

@app.get("/")
async def root():
    return {"message": "🚀 Smart RAG API running locally! Upload & ask questions freely."}

@app.get("/health")
async def health():
    return {"status": "healthy", "documents_indexed": os.path.exists("vectorstore/faiss_index")}

@app.post("/clear")
async def clear_vectorstore():
    if os.path.exists(VECTORSTORE_DIR):
        shutil.rmtree(VECTORSTORE_DIR)
        os.makedirs(VECTORSTORE_DIR)
    return {"message": "Vector store cleared!"}

@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")

    file_id = str(uuid.uuid4())
    safe_filename = f"{file_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        loader = get_document_loader(file.filename, file_path)
        documents = loader.load() if not isinstance(loader, list) else loader
        chunks = split_docs(documents)
        add_document_to_vectorstore(chunks, file.filename)

        return UploadResponse(
            file_id=file_id,
            filename=file.filename,
            message=f"'{file.filename}' uploaded and indexed successfully!"
        )
    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail="Failed to process file")

@app.post("/query", response_model=QueryResponse)
async def query_document(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    question = request.question
    lower_question = question.lower()

    chain = get_qa_chain()
    if chain is None:
        raise HTTPException(status_code=400, detail="No documents uploaded yet. Please upload a document first.")

    try:
        # Case 1: User wants to extract raw text from images (any phrasing)
        extraction_keywords = [
            "extract text", "read text", "all text", "what is written", "text from", 
            "read the text", "give me text", "show text", "get text", "text in the image",
            "what does it say", "ocr text"
        ]
        if any(keyword in lower_question for keyword in extraction_keywords):
            # Dummy query to get all relevant chunks
            result = chain.invoke({"query": "text from images or photos"})
            image_texts = []
            sources = []
            for doc in result["source_documents"]:
                source = doc.metadata.get("source", "").lower()
                if source.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                    image_texts.append(doc.page_content.strip())
                    sources.append({
                        "file": doc.metadata.get("source", "Unknown"),
                        "page": doc.metadata.get("page", "N/A"),
                        "preview": doc.page_content[:300]
                    })
            
            if image_texts:
                full_text = "\n\n".join(image_texts)
                return QueryResponse(
                    answer=f"Extracted text from the uploaded image(s):\n\n{full_text}",
                    sources=sources
                )
            else:
                return QueryResponse(
                    answer="No readable text found in any uploaded image.",
                    sources=[]
                )

        # Case 2: Image-related questions (headline, summarize, explain, etc.)
        image_keywords = ["image", "photo", "picture", "jpg", "png", "screenshot", "diagram", "chart", "news in the image", "headline", "summarize the image"]
        if any(keyword in lower_question for keyword in image_keywords):
            # Boost image relevance
            enhanced_query = question + " (from uploaded image or photo)"
            result = chain.invoke({"query": enhanced_query})
        else:
            # Case 3: Normal RAG query for PDF, DOCX, etc.
            result = chain.invoke({"query": question})

        # Common response formatting
        sources = [
            {
                "file": doc.metadata.get("source", "Unknown"),
                "page": doc.metadata.get("page", "N/A"),
                "preview": doc.page_content[:250] + ("..." if len(doc.page_content) > 250 else "")
            }
            for doc in result["source_documents"]
        ]

        answer = result["result"].strip()
        # Improve "not found" message
        if "not found" in answer.lower() or "no information" in answer.lower() or not answer:
            answer = "I couldn't find relevant information for your question in the uploaded documents."

        return QueryResponse(answer=answer, sources=sources)

    except Exception as e:
        logger.error(f"Query error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate answer. Please try again.")