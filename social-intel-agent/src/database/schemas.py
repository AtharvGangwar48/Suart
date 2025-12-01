from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class AnalysisResult(BaseModel):
    url: str
    platform: str
    content: Dict
    sentiment: Optional[Dict] = None
    toxicity: Optional[Dict] = None
    hate_speech: Optional[Dict] = None
    risk_score: Optional[Dict] = None
    created_at: datetime
    
class CacheEntry(BaseModel):
    key: str
    value: Dict
    ttl: int
    created_at: datetime