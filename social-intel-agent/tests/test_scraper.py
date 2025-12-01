import pytest
from src.services.scraper_service import ScraperService

class TestScraperService:
    def setup_method(self):
        self.scraper = ScraperService()
    
    @pytest.mark.asyncio
    async def test_scrape_valid_url(self):
        url = "https://example.com"
        result = await self.scraper.scrape(url)
        assert result is not None
        assert "url" in result
    
    def test_scraper_initialization(self):
        assert self.scraper is not None
        assert hasattr(self.scraper, 'scraper')
        assert hasattr(self.scraper, 'extractor')