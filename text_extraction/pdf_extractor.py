import pdfplumber


def extract_pdf(file_path: str) -> str:
    """
    Extract PDF text with page boundaries preserved.
    """

    full_text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text.strip()

            # 🔑 PAGE SEPARATOR
            full_text += "\f"

    return full_text
