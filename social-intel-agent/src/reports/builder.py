from datetime import datetime
from src.utils.formatter import Formatter

class ReportBuilder:
    def __init__(self):
        self.formatter = Formatter()
    
    def build_report(self, content: dict, risk_score: dict):
        report = {
            "analysis_id": hash(str(content) + str(datetime.utcnow())),
            "timestamp": self.formatter.format_timestamp(datetime.utcnow()),
            "url": content.get("url", ""),
            "platform": content.get("platform", "unknown"),
            "risk_assessment": {
                "level": risk_score.get("level", "UNKNOWN"),
                "score": risk_score.get("score", 0),
                "factors": risk_score.get("factors", [])
            },
            "content_analysis": content,
            "summary": self._generate_summary(content, risk_score)
        }
        
        return report
    
    def _generate_summary(self, content: dict, risk_score: dict):
        risk_level = risk_score.get("level", "UNKNOWN")
        platform = content.get("platform", "unknown")
        
        summary = f"Analysis of {platform} content shows {risk_level.lower()} risk level."
        
        if risk_score.get("factors"):
            factors = ", ".join(risk_score["factors"])
            summary += f" Risk factors identified: {factors}."
        
        return summary