"""Placeholder anonymization layer.

Step 8 of the plan: swap this out for a real Anymize AI call. Until then,
these are identity pass-through functions so the rest of the pipeline can be
built and tested end-to-end without the dependency blocking progress.
"""


def anonymize(text: str) -> tuple[str, dict]:
    """Return (masked_text, restore_map). No-op for now."""
    return text, {}


def restore(text: str, restore_map: dict) -> str:
    """Reverse anonymize(). No-op for now."""
    return text
