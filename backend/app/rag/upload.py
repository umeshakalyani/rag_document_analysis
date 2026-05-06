from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_parser import extract_pdf_text
from app.services.chunker import chunk_text

from app.rag.embeddings import create_embeddings
from app.rag.vector_store import store_embeddings

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_pdf_text(file_path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    store_embeddings(chunks, embeddings)

    return {
        "message": "Document uploaded successfully"
    }