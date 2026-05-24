from backend.database.db import get_connection


def create_chat(title="New Chat"):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chats (title)
        VALUES (?)
        """,
        (title,)
    )

    chat_id = cursor.lastrowid

    conn.commit()

    conn.close()

    return chat_id


def get_all_chats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, title
    FROM chats
    ORDER BY id DESC
    """)

    chats = cursor.fetchall()

    conn.close()

    return chats


def save_message(chat_id, role, content):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages
        (chat_id, role, content)

        VALUES (?, ?, ?)
        """,
        (chat_id, role, content)
    )

    conn.commit()

    conn.close()


def load_chat_messages(chat_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE chat_id = ?
        ORDER BY id ASC
        """,
        (chat_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    messages = []

    for row in rows:

        messages.append({
            "role": row[0],
            "content": row[1]
        })

    return messages