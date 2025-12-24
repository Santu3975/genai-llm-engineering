import re


def clean_text(text: str) -> str:
    """
    Light cleaning only.
    DO NOT destroy structure (production-safe).
    """

    if not text:
        return ""

    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
