import pytest
from src.services.ocr_service import OCRService
from unittest.mock import patch, MagicMock

class TestOCRService:
    def setup_method(self):
        self.ocr = OCRService()
    
    @patch('src.services.ocr_service.pytesseract.image_to_string')
    @patch('src.services.ocr_service.Image.open')
    def test_extract_text_success(self, mock_image_open, mock_tesseract):
        mock_tesseract.return_value = "Sample text from image"
        mock_image_open.return_value = MagicMock()
        
        result = self.ocr.extract_text_from_image("test_image.jpg")
        assert result == "Sample text from image"
    
    @patch('src.services.ocr_service.pytesseract.image_to_string')
    @patch('src.services.ocr_service.Image.open')
    def test_extract_text_failure(self, mock_image_open, mock_tesseract):
        mock_tesseract.side_effect = Exception("OCR failed")
        
        result = self.ocr.extract_text_from_image("invalid_image.jpg")
        assert result == ""