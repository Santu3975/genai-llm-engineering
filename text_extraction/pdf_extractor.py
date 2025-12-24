from pypdf import PdfReader


def extract_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        str: Extracted text content
    """
    reader = PdfReader(file_path)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text.append(text.strip())

    return "\n\n".join(extracted_text)


if __name__ == "__main__":
    # Example usage
    pdf_path = "sample.pdf"
    text = extract_pdf(pdf_path)
    print(text[:1000])  # preview first 1000 characters
