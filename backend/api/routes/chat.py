from fastapi import APIRouter
from pydantic import BaseModel

from backend.agents.chat_agent import generate_response

from backend.memory.short_term import (
    create_chat,
    get_all_chats,
    load_chat_messages
)

router = APIRouter()


class ChatRequest(BaseModel):
    chat_id: int
    message: str


@router.post("/chat/new")
def new_chat():

    chat_id = create_chat()

    return {
        "chat_id": chat_id
    }


@router.get("/chats")
def chats():

    chats = get_all_chats()

    return {
        "chats": chats
    }


@router.get("/chat/{chat_id}")
def get_chat(chat_id: int):

    messages = load_chat_messages(chat_id)

    return {
        "messages": messages
    }


@router.post("/chat")
async def chat(request: ChatRequest):

    response = await generate_response(
        request.chat_id,
        request.message
    )

    return {
        "response": response
    }