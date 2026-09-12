import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import db, llm

app = FastAPI(title="AI Journaling & Biography")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    db.init_db()


# ---------- Schemas ----------

class ChatTurn(BaseModel):
    history: list[dict]  # [{"role": "user"|"assistant", "content": str}]


class SaveJournalRequest(BaseModel):
    history: list[dict]


class PersonCreate(BaseModel):
    name: str
    relationship: str | None = None


class MemoryCreate(BaseModel):
    content: str
    source_journal_id: int | None = None


class BiographyRequest(BaseModel):
    entry_ids: list[int] | None = None  # None = use all entries


# ---------- Journal conversation ----------

@app.post("/api/chat")
def chat(turn: ChatTurn):
    reply = llm.chat_reply(turn.history)
    return {"reply": reply}


@app.post("/api/journal")
def save_journal(req: SaveJournalRequest):
    conversation_text = "\n".join(
        f"{m['role']}: {m['content']}" for m in req.history
    )
    extracted = llm.extract_journal(conversation_text)

    conn = db.get_connection()
    cur = conn.execute(
        "INSERT INTO journal_entries (title, content, raw_conversation, themes) "
        "VALUES (?, ?, ?, ?)",
        (
            extracted["title"],
            extracted["journal_entry"],
            conversation_text,
            json.dumps(extracted.get("themes", [])),
        ),
    )
    conn.commit()
    entry_id = cur.lastrowid
    conn.close()

    return {"id": entry_id, **extracted}


@app.get("/api/journal")
def list_journal():
    conn = db.get_connection()
    rows = conn.execute(
        "SELECT * FROM journal_entries ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# ---------- Patterns ----------

@app.post("/api/patterns")
def find_patterns():
    conn = db.get_connection()
    rows = conn.execute(
        "SELECT * FROM journal_entries ORDER BY created_at ASC"
    ).fetchall()
    conn.close()

    if len(rows) < 2:
        raise HTTPException(
            status_code=400,
            detail="Need at least 2 journal entries to detect patterns.",
        )

    entries = [dict(r) for r in rows]
    return llm.detect_patterns(entries)


# ---------- Family tree ----------

@app.post("/api/persons")
def create_person(person: PersonCreate):
    conn = db.get_connection()
    cur = conn.execute(
        "INSERT INTO persons (name, relationship) VALUES (?, ?)",
        (person.name, person.relationship),
    )
    conn.commit()
    person_id = cur.lastrowid
    conn.close()
    return {"id": person_id, "name": person.name, "relationship": person.relationship}


@app.get("/api/persons")
def list_persons():
    conn = db.get_connection()
    persons = conn.execute("SELECT * FROM persons").fetchall()
    result = []
    for p in persons:
        memories = conn.execute(
            "SELECT * FROM memories WHERE person_id = ?", (p["id"],)
        ).fetchall()
        result.append({**dict(p), "memories": [dict(m) for m in memories]})
    conn.close()
    return result


@app.post("/api/persons/{person_id}/memories")
def add_memory(person_id: int, memory: MemoryCreate):
    conn = db.get_connection()
    person = conn.execute(
        "SELECT id FROM persons WHERE id = ?", (person_id,)
    ).fetchone()
    if not person:
        conn.close()
        raise HTTPException(status_code=404, detail="Person not found")

    cur = conn.execute(
        "INSERT INTO memories (person_id, content, source_journal_id) VALUES (?, ?, ?)",
        (person_id, memory.content, memory.source_journal_id),
    )
    conn.commit()
    memory_id = cur.lastrowid
    conn.close()
    return {"id": memory_id, "person_id": person_id, "content": memory.content}


# ---------- Biography ----------

@app.post("/api/biography")
def generate_biography(req: BiographyRequest):
    conn = db.get_connection()
    if req.entry_ids:
        placeholders = ",".join("?" * len(req.entry_ids))
        rows = conn.execute(
            f"SELECT * FROM journal_entries WHERE id IN ({placeholders})",
            req.entry_ids,
        ).fetchall()
    else:
        rows = conn.execute("SELECT * FROM journal_entries").fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=400, detail="No journal entries available.")

    entries = [dict(r) for r in rows]
    patterns = llm.detect_patterns(entries) if len(entries) >= 2 else {"patterns": []}
    chapter = llm.generate_biography_chapter(entries, patterns)
    return {"chapter": chapter, "patterns": patterns}


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
