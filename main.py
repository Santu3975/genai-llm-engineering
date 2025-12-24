import os

# -------- EXTRACTION IMPORTS --------
from extractors.txt_extractor import extract_txt
from extractors.pdf_extractor import extract_pdf
from extractors.docx_extractor import extract_docx
from extractors.excel_extractor import extract_excel
from extractors.image_extractor import extract_image
from extractors.cleaner import clean_text

# -------- CHUNKING IMPORTS --------
from chunking.chunking_methods import (
    fixed_size_chunking,
    recursive_chunking,
    document_based_chunking,
    semantic_chunking,
    page_level_chunking
)


# -------- EXTRACTION CONTROLLER --------
def extract_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        text = extract_txt(file_path)
    elif ext == ".pdf":
        text = extract_pdf(file_path)
    elif ext == ".docx":
        text = extract_docx(file_path)
    elif ext in [".xlsx", ".xls"]:
        text = extract_excel(file_path)
    elif ext in [".png", ".jpg", ".jpeg"]:
        text = extract_image(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return clean_text(text)


# -------- MAIN EXECUTION --------
if __name__ == "__main__":

    file_path = "data/sample.pdf"

    # ===== EXTRACTION =====
    text = extract_text(file_path)

    print("\n========== EXTRACTION OUTPUT ==========")
    print("FILE:", file_path)
    print("TEXT LENGTH:", len(text))
    print("PAGE BREAK COUNT:", text.count("\f"))
    print("PREVIEW:\n", text[:300])

    # ===== PAGE LEVEL CHUNKING =====
    page_chunks = page_level_chunking(text)

    print("\n========== PAGE LEVEL CHUNKING ==========")
    print("Total page chunks:", len(page_chunks))

    # 🔹 PRINT ALL PAGES
    for i, page in enumerate(page_chunks, start=1):
        print(f"\n---------- FULL PAGE {i} ----------\n")
        print(page)

    # 🔹 SAVE PAGES TO FILES (BEST PRACTICE)
    os.makedirs("page_outputs", exist_ok=True)

    for i, page in enumerate(page_chunks, start=1):
        with open(f"page_outputs/page_{i}.txt", "w", encoding="utf-8") as f:
            f.write(page)

    print("\nSaved page chunks to 'page_outputs/' folder.")

    # ===== OTHER CHUNKING METHODS =====
    print("\n========== FIXED SIZE CHUNKING ==========")
    print("Total chunks:", len(fixed_size_chunking(text)))

    print("\n========== RECURSIVE CHUNKING ==========")
    print("Total chunks:", len(recursive_chunking(text)))

    print("\n========== DOCUMENT BASED CHUNKING ==========")
    print("Total chunks:", len(document_based_chunking(text)))

    print("\n========== SEMANTIC CHUNKING ==========")
    print("Total chunks:", len(semantic_chunking(text)))
