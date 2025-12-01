from transformers import pipeline

class ToxicityDetector:
    def __init__(self):
        self.classifier = pipeline("text-classification", 
                                 model="unitary/toxic-bert")
    
    def detect(self, text: str):
        result = self.classifier(text)
        return {
            "is_toxic": result[0]["label"] == "TOXIC",
            "confidence": result[0]["score"]
        }