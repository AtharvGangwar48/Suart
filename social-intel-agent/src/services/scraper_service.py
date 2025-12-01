from src.scraping.playwright_scraper import PlaywrightScraper
from src.scraping.extractors import ContentExtractor

class ScraperService:
    def __init__(self):
        self.scraper = PlaywrightScraper()
        self.extractor = ContentExtractor()
    
    async def scrape(self, url: str):
        raw_html = await self.scraper.scrape_page(url)
        content = self.extractor.extract_content(raw_html, url)
        return content