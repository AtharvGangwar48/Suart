import pytest
from src.analysis.text.sentiment import SentimentAnalyzer

class TestSentimentAnalyzer:
    def setup_method(self):
        self.analyzer = SentimentAnalyzer()
    
    def test_positive_sentiment(self):
        text = "I love this amazing product!"
        result = self.analyzer.analyze(text)
        assert "label" in result
        assert "score" in result
        assert isinstance(result["score"], float)
    
    def test_negative_sentiment(self):
        text = "This is terrible and awful"
        result = self.analyzer.analyze(text)
        assert "label" in result
        assert "score" in result