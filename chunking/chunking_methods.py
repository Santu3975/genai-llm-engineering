import re

# ---------- FIXED SIZE CHUNKING ----------
def fixed_size_chunking(text, chunk_size=200, overlap=40):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


# ---------- RECURSIVE CHUNKING ----------
def recursive_chunking(text, max_size=200):
    separators = ["\n\n", "\n", ". ", " "]
    chunks = [text]

    for sep in separators:
        new_chunks = []
        for chunk in chunks:
            if len(chunk) > max_size:
                new_chunks.extend(chunk.split(sep))
            else:
                new_chunks.append(chunk)
        chunks = new_chunks

    final_chunks = []
    for c in chunks:
        if len(c) > max_size:
            for i in range(0, len(c), max_size):
                final_chunks.append(c[i:i + max_size])
        else:
            final_chunks.append(c)

    return [c.strip() for c in final_chunks if c.strip()]


# ---------- DOCUMENT BASED CHUNKING ----------
def document_based_chunking(text):
    sections = re.split(r"\n[A-Z][A-Z\s]{3,}\n", text)
    return [s.strip() for s in sections if s.strip()]


# ---------- SEMANTIC CHUNKING ----------
def semantic_chunking(text, sentences_per_chunk=3):
    sentences = text.split(". ")
    chunks = []
    buffer = []

    for s in sentences:
        buffer.append(s)
        if len(buffer) >= sentences_per_chunk:
            chunks.append(". ".join(buffer))
            buffer = []

    if buffer:
        chunks.append(". ".join(buffer))

    return chunks


# ---------- PAGE LEVEL CHUNKING ----------
def page_level_chunking(text):
    """
    Each PDF page becomes one chunk.
    Requires page separators (\f) from extractor.
    """

    pages = text.split("\f")
    return [page.strip() for page in pages if page.strip()]


