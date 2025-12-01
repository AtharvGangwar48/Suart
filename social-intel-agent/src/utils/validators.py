import re
from urllib.parse import urlparse

class Validators:
    @staticmethod
    def is_valid_url(url: str) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    @staticmethod
    def is_social_media_url(url: str) -> bool:
        social_domains = [
            'youtube.com', 'instagram.com', 'twitter.com', 
            'x.com', 'reddit.com', 'tiktok.com', 'facebook.com'
        ]
        
        try:
            domain = urlparse(url).netloc.replace('www.', '')
            return any(social_domain in domain for social_domain in social_domains)
        except:
            return False
    
    @staticmethod
    def validate_file_extension(filename: str, allowed_extensions: list) -> bool:
        extension = filename.split('.')[-1].lower()
        return extension in allowed_extensions