import hashlib
from src.database.redis_cache import RedisCache

class HashingService:
    def __init__(self):
        self.cache = RedisCache()
    
    def generate_content_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()
    
    def check_duplicate(self, content_hash: str) -> bool:
        return self.cache.exists(content_hash)