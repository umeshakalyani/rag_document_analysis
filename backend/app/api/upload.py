from fastapi import APIRouter, UploadFile, File
import os

from app.services.docx_parser import extract_docx_text
from app.services.chunker import chunk_text

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = ""

    if file.filename.endswith(".docx"):

        text = extract_docx_text(file_path)

    chunks = chunk_text(text)

    return {
        "message": "Document processed successfully",
        "filename": file.filename,
        "characters": len(text),
        "chunks": len(chunks),
        "preview": text[:300]
    }