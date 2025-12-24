from PIL import Image
import pytesseract

def extract_image(file_path: str) -> str:
    img = Image.open(file_path)
    return pytesseract.image_to_string(img)
