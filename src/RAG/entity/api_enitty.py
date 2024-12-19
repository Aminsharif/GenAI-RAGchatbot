from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str, Enum):
    gemma2_9b_it = "gemma2-9b-it"
    llama3_groq_70b = "llama3-groq-70b-8192-tool-use-preview"
    llama3_groq_8b="llama3-groq-8b-8192-tool-use-preview"
    llama_3_1_70b="llama-3.1-70b-versatile"
    llama_3_2_11b="llama-3.2-11b-vision-preview"
    llama_3_3_70b = "llama-3.3-70b-specdec"
    llama_3_3_70b_versatile = "llama-3.3-70b-versatile"
    mixtral = "mixtral-8x7b-32768"
    llama_3_2_90b = "llama-3.2-90b-vision-preview"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.llama_3_3_70b_versatile)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int