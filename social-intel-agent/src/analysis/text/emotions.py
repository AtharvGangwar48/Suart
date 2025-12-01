from transformers import pipeline

class EmotionClassifier:
    def __init__(self):
        self.classifier = pipeline("text-classification",
                                 model="j-hartmann/emotion-english-distilroberta-base")
    
    def classify(self, text: str):
        result = self.classifier(text)
        return {
            "emotion": result[0]["label"],
            "confidence": result[0]["score"]
        }