from transformers import pipeline
from PIL import Image

class VisionClassifier:
    def __init__(self):
        self.nsfw_classifier = pipeline("image-classification",
                                      model="Falconsai/nsfw_image_detection")
    
    def classify_image(self, image_path: str):
        image = Image.open(image_path)
        result = self.nsfw_classifier(image)
        
        return {
            "is_nsfw": result[0]["label"] == "nsfw",
            "confidence": result[0]["score"]
        }