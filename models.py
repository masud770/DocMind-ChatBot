from pydantic import BaseModel
from typing import List, Optional

class UploadResponse(BaseModel):
    file_id: str
    filename: str
    message: str

class QueryRequest(BaseModel):
    question: str
    image_base64: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[dict]