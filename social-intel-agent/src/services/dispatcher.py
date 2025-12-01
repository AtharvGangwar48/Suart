from src.services.scraper_service import ScraperService
from src.services.summarizer import Summarizer
from src.analysis.scoring.risk_score import RiskScorer

class AnalysisDispatcher:
    def __init__(self):
        self.scraper = ScraperService()
        self.summarizer = Summarizer()
        self.risk_scorer = RiskScorer()
    
    async def analyze(self, url: str, deep_analysis: bool = False):
        # Scrape content
        content = await self.scraper.scrape(url)
        
        # Analyze and score
        risk_score = self.risk_scorer.calculate(content)
        
        # Generate report
        report = self.summarizer.generate_report(content, risk_score)
        
        return report