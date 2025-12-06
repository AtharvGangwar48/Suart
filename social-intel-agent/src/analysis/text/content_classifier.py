from transformers import pipeline
import re

class ContentClassifier:
    """Multi-category content classifier"""
    
    def __init__(self):
        # Use zero-shot classification for multiple categories
        try:
            self.classifier = pipeline("zero-shot-classification", 
                                     model="facebook/bart-large-mnli")
        except:
            self.classifier = None
    
    def classify(self, text: str):
        """Classify text into multiple content categories"""
        
        categories = [
            "hateful speech",
            "terrorism or violence",
            "religious extremism",
            "sexual content",
            "abusive language",
            "drug related",
            "spam or scam",
            "normal content"
        ]
        
        if not self.classifier or not text or len(text) < 10:
            return self._get_default_result()
        
        try:
            # Truncate text for analysis
            analysis_text = text[:512]
            
            # Run zero-shot classification
            result = self.classifier(analysis_text, categories, multi_label=True)
            
            # Build category scores
            category_scores = {}
            detected_categories = []
            
            for label, score in zip(result['labels'], result['scores']):
                category_key = self._normalize_category(label)
                category_scores[category_key] = round(score, 3)
                
                # Flag if confidence > 0.5 and not normal content
                if score > 0.5 and label != "normal content":
                    detected_categories.append(category_key)
            
            # Determine primary category (highest score excluding normal)
            primary_category = "normal"
            max_score = 0.0
            
            for label, score in zip(result['labels'], result['scores']):
                if label != "normal content" and score > max_score:
                    max_score = score
                    primary_category = self._normalize_category(label)
            
            # If highest non-normal score is low, classify as normal
            if max_score < 0.4:
                primary_category = "normal"
                detected_categories = []
            
            return {
                "primary_category": primary_category,
                "detected_categories": detected_categories,
                "category_scores": category_scores,
                "is_flagged": len(detected_categories) > 0
            }
            
        except Exception as e:
            return self._get_default_result()
    
    def _normalize_category(self, label: str) -> str:
        """Normalize category labels"""
        mapping = {
            "hateful speech": "hateful",
            "terrorism or violence": "terror",
            "religious extremism": "religious",
            "sexual content": "sexual",
            "abusive language": "abusive",
            "drug related": "drug",
            "spam or scam": "spam",
            "normal content": "normal"
        }
        return mapping.get(label, label)
    
    def _get_default_result(self):
        """Return default result when classifier unavailable"""
        return {
            "primary_category": "normal",
            "detected_categories": [],
            "category_scores": {},
            "is_flagged": False
        }
