import os
import json
import pandas as pd
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader, TextLoader, CSVLoader
)
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PIL import Image
from io import BytesIO
import base64
import easyocr

reader = easyocr.Reader(['en', 'bn'], gpu=False)

def get_document_loader(filename: str, file_path: str):
    ext = os.path.splitext(filename)[1].lower()

    if ext == ".pdf":
        return PyPDFLoader(file_path)
    elif ext == ".docx":
        return Docx2txtLoader(file_path)
    elif ext == ".txt":
        return TextLoader(file_path, encoding="utf-8")
    elif ext == ".csv":
        return CSVLoader(file_path)
    elif ext == ".json":
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            text = json.dumps(data, indent=2, ensure_ascii=False)
            return [Document(page_content=text, metadata={"source": filename})]
        except:
            raise ValueError("Invalid JSON file")
    elif ext in [".xlsx", ".xls"]:
        try:
            df = pd.read_excel(file_path)
            text = df.to_string(index=False)
            return [Document(page_content=text, metadata={"source": filename})]
        except Exception as e:
            raise ValueError(f"Cannot read Excel file: {e}")
    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        result = reader.readtext(file_path, detail=0, paragraph=True)
        text = "\n".join(result)
        return [Document(page_content=text, metadata={"source": filename})]
    else:
        # Fallback: try to read as plain text
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            return [Document(page_content=text, metadata={"source": filename})]
        except:
            raise ValueError(f"Unsupported file type: {ext}")

def split_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_documents(documents)

def ocr_from_base64(image_base64: str) -> str:
    try:
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        result = reader.readtext(image, detail=0, paragraph=True)
        return "\n".join(result).strip()
    except Exception as e:
        return f"OCR failed: {str(e)}"