import requests
from pathlib import Path
from src.config.constants import MAX_FILE_SIZE

class Downloader:
    def __init__(self, download_dir: str = "temp/downloads"):
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)
    
    def download_file(self, url: str, filename: str = None):
        response = requests.head(url)
        content_length = int(response.headers.get('content-length', 0))
        
        if content_length > MAX_FILE_SIZE:
            raise ValueError(f"File too large: {content_length} bytes")
        
        if not filename:
            filename = url.split('/')[-1]
        
        filepath = self.download_dir / filename
        
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        return filepath