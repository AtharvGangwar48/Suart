from datetime import datetime, timedelta
import time

class TimeUtils:
    @staticmethod
    def get_current_timestamp() -> datetime:
        return datetime.utcnow()
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            return f"{seconds/60:.1f}m"
        else:
            return f"{seconds/3600:.1f}h"
    
    @staticmethod
    def is_expired(timestamp: datetime, ttl_seconds: int) -> bool:
        expiry_time = timestamp + timedelta(seconds=ttl_seconds)
        return datetime.utcnow() > expiry_time
    
    @staticmethod
    def sleep_with_backoff(attempt: int, base_delay: float = 1.0):
        delay = base_delay * (2 ** attempt)
        time.sleep(min(delay, 60))  # Max 60 seconds