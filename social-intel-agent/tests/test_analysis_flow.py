import pytest
from src.services.dispatcher import AnalysisDispatcher

class TestAnalysisFlow:
    def setup_method(self):
        self.dispatcher = AnalysisDispatcher()
    
    @pytest.mark.asyncio
    async def test_full_analysis_flow(self):
        url = "https://example.com"
        result = await self.dispatcher.analyze(url)
        
        assert result is not None
        assert isinstance(result, dict)
    
    def test_dispatcher_initialization(self):
        assert self.dispatcher is not None
        assert hasattr(self.dispatcher, 'scraper')
        assert hasattr(self.dispatcher, 'summarizer')
        assert hasattr(self.dispatcher, 'risk_scorer')