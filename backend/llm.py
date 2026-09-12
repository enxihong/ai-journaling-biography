import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    return _client


MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")


def chat_reply(history: list[dict]) -> str:
    """One conversational follow-up turn. history is a list of {role, content}."""
    system = {
        "role": "system",
        "content": (
            "You are a warm, low-friction journaling companion. Ask ONE short "
            "follow-up question at a time to help the user recall a meaningful "
            "memory. Never invent facts the user hasn't stated. If the user "
            "seems done, tell them they can save the entry now."
        ),
    }
    resp = get_client().chat.completions.create(
        model=MODEL,
        messages=[system, *history],
        temperature=0.7,
    )
    return resp.choices[0].message.content


def extract_journal(conversation_text: str) -> dict:
    """Turn a raw conversation transcript into a structured journal entry."""
    system = {
        "role": "system",
        "content": (
            "Convert the conversation transcript into a structured journal "
            "entry. Only use facts present in the transcript - never invent "
            "names, dates, or events. Respond with JSON matching this shape: "
            '{"title": str, "journal_entry": str, "people": [str], '
            '"themes": [str], "events": [str]}'
        ),
    }
    user = {"role": "user", "content": conversation_text}
    resp = get_client().chat.completions.create(
        model=MODEL,
        messages=[system, user],
        temperature=0.3,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


def detect_patterns(entries: list[dict]) -> dict:
    """Find recurring themes/behaviors across multiple journal entries."""
    joined = "\n\n---\n\n".join(
        f"[{e['created_at']}] {e['title']}\n{e['content']}" for e in entries
    )
    system = {
        "role": "system",
        "content": (
            "You are analyzing someone's journal entries to find genuine "
            "recurring patterns - specific, personal observations, not "
            "generic platitudes. Only point to patterns actually supported "
            "by the text below. Respond with JSON: "
            '{"patterns": [{"pattern": str, "evidence": [str]}]}'
        ),
    }
    user = {"role": "user", "content": joined}
    resp = get_client().chat.completions.create(
        model=MODEL,
        messages=[system, user],
        temperature=0.4,
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


def generate_biography_chapter(entries: list[dict], patterns: dict) -> str:
    """Draft one biography chapter using only the given entries/patterns as sources."""
    joined = "\n\n---\n\n".join(
        f"[{e['created_at']}] {e['title']}\n{e['content']}" for e in entries
    )
    pattern_text = "\n".join(f"- {p['pattern']}" for p in patterns.get("patterns", []))
    system = {
        "role": "system",
        "content": (
            "Using ONLY the journal entries and patterns provided below, "
            "write one warm, narrative biography chapter. Do not add any "
            "facts, dates, or quotes that are not present in the sources. "
            "If details are uncertain, phrase them as such (e.g. 'around "
            "that time', 'as they remember it')."
        ),
    }
    user = {
        "role": "user",
        "content": f"Journal entries:\n{joined}\n\nObserved patterns:\n{pattern_text}",
    }
    resp = get_client().chat.completions.create(
        model=MODEL,
        messages=[system, user],
        temperature=0.6,
    )
    return resp.choices[0].message.content
