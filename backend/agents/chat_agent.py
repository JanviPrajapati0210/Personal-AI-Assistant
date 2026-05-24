import ollama

from backend.memory.short_term import (
    save_message,
    load_chat_messages
)

from backend.tools.tool_router import (
    handle_tools
)

SYSTEM_PROMPT = """
You are a powerful AI assistant.
"""

async def generate_response(
    chat_id,
    user_message
):

    save_message(
        chat_id,
        "user",
        user_message
    )

    # TOOL CHECK
    tool_result = handle_tools(user_message)

    if tool_result:

        save_message(
            chat_id,
            "assistant",
            tool_result
        )

        return tool_result

    # NORMAL AI CHAT
    messages = load_chat_messages(chat_id)

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + messages
    )

    ai_response = response["message"]["content"]

    save_message(
        chat_id,
        "assistant",
        ai_response
    )

    return ai_response