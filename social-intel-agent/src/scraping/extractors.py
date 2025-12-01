from urllib.parse import urlparse
from src.scraping.html_parser import HTMLParser
from src.scraping.selectors import youtube, instagram, reddit, twitter, generic

class ContentExtractor:
    def __init__(self):
        self.parser = HTMLParser()
        self.platform_selectors = {
            "youtube.com": youtube.YOUTUBE_SELECTORS,
            "instagram.com": instagram.INSTAGRAM_SELECTORS,
            "reddit.com": reddit.REDDIT_SELECTORS,
            "twitter.com": twitter.TWITTER_SELECTORS,
            "x.com": twitter.TWITTER_SELECTORS
        }
    
    def extract_content(self, html_content: str, url: str):
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace("www.", "")
        
        # Get platform-specific selectors or use generic
        selectors = self.platform_selectors.get(domain, generic.GENERIC_SELECTORS)
        
        # Parse HTML content
        parsed_content = self.parser.parse_html(html_content)
        
        return {
            "url": url,
            "platform": domain,
            "content": parsed_content,
            "selectors_used": selectors
        }