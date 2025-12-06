from src.services.universal_scraper_service import UniversalScraperService
from src.analysis.text.sentiment import SentimentAnalyzer
from src.analysis.text.toxicity import ToxicityDetector
from src.analysis.text.hate_speech import HateSpeechDetector
from src.analysis.text.content_classifier import ContentClassifier
from src.analysis.scoring.risk_score import RiskScorer
from src.config.logger import setup_logger
import uuid
from datetime import datetime

logger = setup_logger(__name__)

class UniversalAnalysisDispatcher:
    """Universal analysis dispatcher with complete AI analysis"""
    
    def __init__(self):
        self.scraper = UniversalScraperService()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.toxicity_detector = ToxicityDetector()
        self.hate_speech_detector = HateSpeechDetector()
        self.content_classifier = ContentClassifier()
        self.risk_scorer = RiskScorer()
    
    async def analyze(self, url: str, deep_analysis: bool = False):
        """Complete analysis pipeline"""
        try:
            # Step 1: Extract content
            logger.info(f"Starting analysis for {url}")
            extracted_data = await self.scraper.scrape(url)
            
            text_content = extracted_data.get("text", "").strip()
            
            if not text_content or len(text_content) < 10:
                return {
                    "analysis_id": str(uuid.uuid4()),
                    "timestamp": datetime.utcnow().isoformat(),
                    "url": url,
                    "platform": extracted_data.get("platform", "unknown"),
                    "status": "error",
                    "message": "No meaningful text content found"
                }
            
            # Truncate for analysis
            analysis_text = text_content[:512]
            
            # Step 2: Sentiment analysis
            logger.info("Analyzing sentiment")
            sentiment = self.sentiment_analyzer.analyze(analysis_text)
            
            # Step 3: Toxicity detection
            logger.info("Detecting toxicity")
            toxicity = self.toxicity_detector.detect(analysis_text)
            
            # Step 4: Hate speech detection
            logger.info("Detecting hate speech")
            hate_speech = self.hate_speech_detector.detect(analysis_text)
            
            # Step 5: Content classification
            logger.info("Classifying content categories")
            content_categories = self.content_classifier.classify(analysis_text)
            
            # Step 6: Calculate risk score
            analysis_data = {
                "sentiment": sentiment,
                "toxicity": toxicity,
                "hate_speech": hate_speech,
                "content_categories": content_categories
            }
            
            risk_assessment = self.risk_scorer.calculate(analysis_data)
            
            # Step 7: Generate report
            report = {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "platform": extracted_data.get("detected_platform", "unknown"),
                "status": "completed",
                "metadata": {
                    "title": extracted_data.get("title", ""),
                    "author": extracted_data.get("author", ""),
                    "published_at": extracted_data.get("published_at", "")
                },
                "risk_assessment": risk_assessment,
                "content_analysis": {
                    "sentiment": sentiment,
                    "toxicity": toxicity,
                    "hate_speech": hate_speech,
                    "content_categories": content_categories
                },
                "summary": self._generate_summary(risk_assessment, sentiment, toxicity, hate_speech, content_categories),
                "text_preview": text_content[:200] + ("..." if len(text_content) > 200 else "")
            }
            
            logger.info(f"Analysis completed with risk level: {risk_assessment['level']}")
            return report
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            return {
                "analysis_id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "url": url,
                "status": "error",
                "message": str(e)
            }
    
    def _generate_summary(self, risk, sentiment, toxicity, hate_speech, content_categories):
        """Generate human-readable summary"""
        parts = []
        
        parts.append(f"Risk Level: {risk['level']} (Score: {risk['score']})")
        parts.append(f"Sentiment: {sentiment['label']} ({sentiment['score']:.2f})")
        
        if toxicity.get('is_toxic'):
            parts.append(f"⚠️ Toxic content detected")
        
        if hate_speech.get('is_hate_speech'):
            parts.append(f"⚠️ Hate speech detected")
        
        if content_categories.get('is_flagged'):
            categories = ", ".join(content_categories.get('detected_categories', []))
            parts.append(f"🚨 Flagged: {categories}")
        
        return " | ".join(parts)
