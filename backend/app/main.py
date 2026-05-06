from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CONNECT ROUTES
app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/")
def home():

    return {
        "message": "RAG API Running"
    }