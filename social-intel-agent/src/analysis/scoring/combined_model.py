import numpy as np

class CombinedScorer:
    def __init__(self):
        self.weights = {
            "sentiment": 0.2,
            "toxicity": 0.3,
            "hate_speech": 0.4,
            "nsfw": 0.1
        }
    
    def calculate_combined_score(self, analysis_results: dict):
        scores = []
        
        for category, weight in self.weights.items():
            if category in analysis_results:
                score = analysis_results[category].get("score", 0)
                weighted_score = score * weight
                scores.append(weighted_score)
        
        combined_score = np.sum(scores) if scores else 0
        
        return {
            "combined_score": combined_score,
            "normalized_score": min(combined_score / 10, 1.0),
            "individual_scores": analysis_results
        }