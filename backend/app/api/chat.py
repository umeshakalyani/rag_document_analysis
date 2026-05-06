from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.query_engine import ask_question

router = APIRouter()

class ChatRequest(BaseModel):

    question: str

@router.post("/chat")
def chat(data: ChatRequest):

    answer = ask_question(data.question)

    return {
        "answer": answer
    }