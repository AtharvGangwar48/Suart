from transformers import pipeline

class HateSpeechDetector:
    def __init__(self):
        try:
            self.classifier = pipeline("text-classification", 
                                     model="facebook/roberta-hate-speech-dynabench-r4-target")
        except:
            # Fallback to simpler model
            self.classifier = None
    
    def detect(self, text: str):
        if not self.classifier:
            return {"is_hate_speech": False, "confidence": 0.0, "label": "unknown"}
        
        result = self.classifier(text[:512])
        is_hate = result[0]["label"] == "hate"
        
        return {
            "is_hate_speech": is_hate,
            "confidence": result[0]["score"],
            "label": result[0]["label"]
        }
