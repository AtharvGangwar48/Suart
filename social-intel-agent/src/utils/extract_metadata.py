from urllib.parse import urlparse
import re

class MetadataExtractor:
    @staticmethod
    def extract_platform_info(url: str):
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '')
        
        platform_info = {
            'domain': domain,
            'path': parsed.path,
            'query': parsed.query
        }
        
        # Extract platform-specific IDs
        if 'youtube.com' in domain:
            video_id = MetadataExtractor._extract_youtube_id(url)
            platform_info['video_id'] = video_id
        elif 'instagram.com' in domain:
            post_id = MetadataExtractor._extract_instagram_id(parsed.path)
            platform_info['post_id'] = post_id
        elif 'reddit.com' in domain:
            subreddit = MetadataExtractor._extract_subreddit(parsed.path)
            platform_info['subreddit'] = subreddit
        
        return platform_info
    
    @staticmethod
    def _extract_youtube_id(url: str):
        pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
        match = re.search(pattern, url)
        return match.group(1) if match else None
    
    @staticmethod
    def _extract_instagram_id(path: str):
        pattern = r'\/p\/([A-Za-z0-9_-]+)'
        match = re.search(pattern, path)
        return match.group(1) if match else None
    
    @staticmethod
    def _extract_subreddit(path: str):
        pattern = r'\/r\/([A-Za-z0-9_]+)'
        match = re.search(pattern, path)
        return match.group(1) if match else None