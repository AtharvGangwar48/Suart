import re

class IntentDetector:
    def __init__(self):
        self.intent_patterns = {
            "promotion": [r"buy", r"sale", r"discount", r"offer"],
            "complaint": [r"terrible", r"awful", r"worst", r"hate"],
            "question": [r"\?", r"how", r"what", r"when", r"where"],
            "information": [r"news", r"update", r"announcement"]
        }
    
    def detect_intent(self, text: str):
        text_lower = text.lower()
        intent_scores = {}
        
        for intent, patterns in self.intent_patterns.items():
            score = sum(1 for pattern in patterns if re.search(pattern, text_lower))
            intent_scores[intent] = score
        
        if not any(intent_scores.values()):
            return {"intent": "general", "confidence": 0.5}
        
        best_intent = max(intent_scores, key=intent_scores.get)
        confidence = intent_scores[best_intent] / len(self.intent_patterns[best_intent])
        
        return {"intent": best_intent, "confidence": min(confidence, 1.0)}