from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

DB_NAME = "users.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.commit()
    conn.close()


class User(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()


@app.post("/users", status_code=201)
def create_user(user: User):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email),
        )
        conn.commit()
        user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Email already exists")
    conn.close()
    return {"id": user_id, "name": user.name, "email": user.email}
