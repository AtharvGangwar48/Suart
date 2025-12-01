import pytesseract
from PIL import Image

class OCRService:
    def extract_text_from_image(self, image_path: str) -> str:
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text.strip()
        except Exception as e:
            return ""