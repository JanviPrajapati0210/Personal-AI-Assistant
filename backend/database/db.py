import sqlite3

DATABASE_NAME = "chat_memory.db"

def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    return conn