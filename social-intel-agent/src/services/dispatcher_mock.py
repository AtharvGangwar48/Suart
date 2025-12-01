class AnalysisDispatcher:
    def __init__(self):
        pass
    
    async def analyze(self, url: str, deep_analysis: bool = False):
        # Mock response for testing
        return {
            "url": url,
            "status": "analyzed",
            "deep_analysis": deep_analysis,
            "risk_score": 0.3,
            "summary": "Mock analysis completed successfully",
            "findings": [
                "Content appears to be safe",
                "No harmful patterns detected"
            ]
        }