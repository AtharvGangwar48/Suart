from transformers import pipeline

class HateSpeechDetector:
    def __init__(self):
        self.classifier = pipeline("text-classification",
                                 model="facebook/roberta-hate-speech-dynabench-r4-target")
    
    def detect(self, text: str):
        result = self.classifier(text)
        return {
            "is_hate_speech": result[0]["label"] == "hate",
            "confidence": result[0]["score"]
        }