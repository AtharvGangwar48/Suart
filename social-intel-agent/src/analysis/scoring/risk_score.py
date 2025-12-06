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
        
        # Content category scores
        categories = content.get("content_categories", {})
        if categories.get("is_flagged"):
            detected = categories.get("detected_categories", [])
            
            if "terror" in detected:
                total_score += 10
                risk_factors.append("terrorism_content")
            
            if "hateful" in detected:
                total_score += 8
                risk_factors.append("hateful_content")
            
            if "sexual" in detected:
                total_score += 6
                risk_factors.append("sexual_content")
            
            if "abusive" in detected:
                total_score += 5
                risk_factors.append("abusive_content")
            
            if "drug" in detected:
                total_score += 7
                risk_factors.append("drug_content")
            
            if "spam" in detected:
                total_score += 3
                risk_factors.append("spam_content")
            
            if "religious" in detected:
                total_score += 6
                risk_factors.append("religious_extremism")
        
        # Media analysis scores
        if content.get("nsfw", {}).get("is_nsfw"):
            total_score += 6
            risk_factors.append("nsfw_content")
        
        # Determine risk level
        if total_score >= 10:
            risk_level = "CRITICAL"
        elif total_score >= 8:
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