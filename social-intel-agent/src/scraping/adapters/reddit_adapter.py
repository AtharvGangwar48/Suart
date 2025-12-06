import requests
from .base_adapter import BaseAdapter

class RedditAdapter(BaseAdapter):
    """Reddit adapter using JSON API"""
    
    async def extract(self, url: str):
        """Extract Reddit post using .json endpoint"""
        json_url = url.rstrip('/') + '.json'
        
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; ContentAnalyzer/1.0)'}
        response = requests.get(json_url, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        post_data = data[0]['data']['children'][0]['data']
        
        # Extract text from post
        text = post_data.get('selftext', '') or post_data.get('title', '')
        
        return self._create_unified_output(
            url=url,
            platform="reddit",
            title=post_data.get('title', ''),
            author=post_data.get('author', ''),
            published_at=str(post_data.get('created_utc', '')),
            text=text,
            meta_description=post_data.get('title', ''),
            media=[]
        )
