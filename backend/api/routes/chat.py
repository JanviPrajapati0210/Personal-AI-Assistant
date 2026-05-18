from fastapi import APIRouter
import ollama

from backend.api.schemas.chat_schema import ChatRequest
from backend.memory.short_term import conversation_history

router = APIRouter()

SYSTEM_PROMPT = """
You are a powerful personal AI assistant.
Be helpful, intelligent, and concise.
"""

@router.post("/chat")
async def chat(user_message: ChatRequest):

    try:

        # Add user message
        conversation_history.append(
            {
                "role": "user",
                "content": user_message.message
            }
        )

        # Build full conversation
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + conversation_history

        # Send to AI
        response = ollama.chat(
            model="llama3",
            messages=messages
        )

        ai_response = response["message"]["content"]

        # Save AI response
        conversation_history.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        return {
            "response": ai_response
        }

    except Exception as e:

        return {
            "error": str(e)
        }