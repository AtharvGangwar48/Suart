import redis
import json
from src.config.settings import settings

class RedisCache:
    def __init__(self):
        self.client = redis.from_url(settings.redis_url)
    
    def get(self, key: str):
        value = self.client.get(key)
        return json.loads(value) if value else None
    
    def set(self, key: str, value: dict, ttl: int = 3600):
        self.client.setex(key, ttl, json.dumps(value))
    
    def exists(self, key: str) -> bool:
        return self.client.exists(key) > 0
    
    def delete(self, key: str):
        self.client.delete(key)