from celery import shared_task
from src.services.dispatcher import AnalysisDispatcher

@shared_task
def analyze_content_async(url: str, deep_analysis: bool = False):
    dispatcher = AnalysisDispatcher()
    result = dispatcher.analyze(url, deep_analysis)
    return result

@shared_task
def scrape_content_async(url: str):
    from src.services.scraper_service import ScraperService
    scraper = ScraperService()
    return scraper.scrape(url)