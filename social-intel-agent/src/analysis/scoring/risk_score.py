from src.config.constants import RISK_LEVELS

class RiskScorer:
    def calculate(self, content: dict):
        risk_factors = []
        total_score = 0
        
        # Text analysis scores
        if content.get("sentiment", {}).get("label") == "NEGATIVE":
            total_score += 2
            risk_factors.append("negative_sentiment")
        
        if content.get("toxicity", {}).get("is_toxic"):
            total_score += 5
            risk_factors.append("toxic_content")
        
        if content.get("hate_speech", {}).get("is_hate_speech"):
            total_score += 8
            risk_factors.append("hate_speech")
        
        # Media analysis scores
        if content.get("nsfw", {}).get("is_nsfw"):
            total_score += 6
            risk_factors.append("nsfw_content")
        
        # Determine risk level
        if total_score >= 8:
            risk_level = "DANGEROUS"
        elif total_score >= 4:
            risk_level = "WARNING"
        else:
            risk_level = "SAFE"
        
        return {
            "score": total_score,
            "level": risk_level,
            "factors": risk_factors
        }