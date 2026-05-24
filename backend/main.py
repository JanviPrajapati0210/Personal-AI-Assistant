from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.chat import router as chat_router
from backend.database.models import create_tables

app = FastAPI()

create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def home():

    return {
        "message": "AI Assistant Running"
    }