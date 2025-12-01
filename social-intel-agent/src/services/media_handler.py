import requests
from pathlib import Path

class MediaHandler:
    def __init__(self):
        self.download_dir = Path("temp/downloads")
        self.download_dir.mkdir(parents=True, exist_ok=True)
    
    async def download_media(self, url: str, media_type: str):
        response = requests.get(url)
        filename = f"{hash(url)}.{media_type}"
        filepath = self.download_dir / filename
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return filepath