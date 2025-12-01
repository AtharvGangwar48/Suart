from src.services.ocr_service import OCRService

class MemeTextExtractor:
    def __init__(self):
        self.ocr = OCRService()
    
    def extract_meme_text(self, image_path: str):
        text = self.ocr.extract_text_from_image(image_path)
        
        # Basic meme text detection
        is_meme = any(word in text.lower() for word in 
                     ["top text", "bottom text", "when", "me when"])
        
        return {
            "text": text,
            "is_meme": is_meme,
            "confidence": 0.8 if is_meme else 0.3
        }