from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.services.universal_dispatcher import UniversalAnalysisDispatcher
from src.analysis.text.sentiment import SentimentAnalyzer
from src.analysis.text.toxicity import ToxicityDetector
from src.analysis.text.hate_speech import HateSpeechDetector
from src.analysis.text.content_classifier import ContentClassifier
from src.analysis.text.intent_detector import IntentDetector
from src.analysis.text.nsfw_detector import NSFWDetector
from src.analysis.image.image_analyzer import ImageAnalyzer
from src.analysis.scoring.risk_score import RiskScorer
import uuid
from datetime import datetime

router = APIRouter(prefix="/analyze", tags=["analysis"])

class DirectAnalyzeRequest(BaseModel):
    text: str
    image_urls: Optional[List[str]] = []
    platform: Optional[str] = "unknown"
    post_url: Optional[str] = ""

@router.post("/direct")
async def analyze_direct(request: DirectAnalyzeRequest):
    """Analyze raw text + images directly (for Chrome extension)"""
    try:
        if not request.text or len(request.text.strip()) < 5:
            raise HTTPException(status_code=400, detail="Text too short to analyze")

        text = request.text[:512]

        sentiment_analyzer = SentimentAnalyzer()
        toxicity_detector = ToxicityDetector()
        hate_speech_detector = HateSpeechDetector()
        content_classifier = ContentClassifier()
        intent_detector = IntentDetector()
        nsfw_detector = NSFWDetector()
        image_analyzer = ImageAnalyzer()
        risk_scorer = RiskScorer()

        sentiment = sentiment_analyzer.analyze(text)
        toxicity = toxicity_detector.detect(text)
        hate_speech = hate_speech_detector.detect(text)
        content_categories = content_classifier.classify(text)
        intent = intent_detector.detect(text)
        nsfw = nsfw_detector.detect(text)

        # Analyze images if provided
        image_analysis = []
        if request.image_urls:
            html = "".join(f'<img src="{u}" />' for u in request.image_urls[:5])
            def analyze_ocr_text(ocr_text):
                return {
                    "sentiment": sentiment_analyzer.analyze(ocr_text[:512]),
                    "toxicity": toxicity_detector.detect(ocr_text[:512]),
                    "hate_speech": hate_speech_detector.detect(ocr_text[:512]),
                    "content_categories": content_classifier.classify(ocr_text[:512]),
                    "risk_assessment": risk_scorer.calculate({
                        "sentiment": sentiment_analyzer.analyze(ocr_text[:512]),
                        "toxicity": toxicity_detector.detect(ocr_text[:512]),
                        "hate_speech": hate_speech_detector.detect(ocr_text[:512]),
                        "content_categories": content_classifier.classify(ocr_text[:512]),
                        "intent": {"intent": "unknown", "confidence": 0},
                        "nsfw": nsfw_detector.detect(ocr_text[:512])
                    })
                }
            image_analysis = image_analyzer.analyze_images(html, request.post_url or "", analyze_ocr_text)

        analysis_data = {
            "sentiment": sentiment,
            "toxicity": toxicity,
            "hate_speech": hate_speech,
            "content_categories": content_categories,
            "intent": intent,
            "nsfw": nsfw,
            "image_analysis": image_analysis
        }

        risk_assessment = risk_scorer.calculate(analysis_data)

        image_risk = 0
        if image_analysis:
            scores = [img.get("image_risk_score", 0) for img in image_analysis]
            image_risk = int(sum(scores) / len(scores))

        text_risk = risk_assessment["score"]
        combined_risk = int(text_risk * 0.6 + image_risk * 0.4) if image_analysis else text_risk

        def get_level(score):
            if score >= 70: return "CRITICAL"
            if score >= 50: return "HIGH"
            if score >= 30: return "MEDIUM"
            if score >= 15: return "LOW"
            return "SAFE"

        return {
            "analysis_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "platform": request.platform,
            "status": "completed",
            "risk_assessment": risk_assessment,
            "combined_risk": {
                "score": combined_risk,
                "level": get_level(combined_risk),
                "text_risk": text_risk,
                "image_risk": image_risk
            },
            "content_analysis": {
                "sentiment": sentiment,
                "toxicity": toxicity,
                "hate_speech": hate_speech,
                "content_categories": content_categories,
                "intent": intent,
                "nsfw": nsfw
            },
            "image_analysis": image_analysis,
            "text_preview": request.text[:200] + ("..." if len(request.text) > 200 else "")
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
