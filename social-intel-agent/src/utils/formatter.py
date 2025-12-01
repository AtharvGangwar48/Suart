from datetime import datetime
import json

class Formatter:
    @staticmethod
    def format_timestamp(dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    
    @staticmethod
    def format_score(score: float) -> str:
        return f"{score:.2f}"
    
    @staticmethod
    def format_json(data: dict) -> str:
        return json.dumps(data, indent=2, default=str)
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 100) -> str:
        return text[:max_length] + "..." if len(text) > max_length else text