from pymongo import MongoClient
from src.config.settings import settings
from datetime import datetime

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(settings.mongo_url)
        self.db = self.client.social_intel
        self.analyses = self.db.analyses
    
    def save_analysis(self, analysis_data: dict):
        analysis_data["created_at"] = datetime.utcnow()
        return self.analyses.insert_one(analysis_data)
    
    def get_analysis(self, analysis_id: str):
        return self.analyses.find_one({"_id": analysis_id})
    
    def get_analyses_by_url(self, url: str):
        return list(self.analyses.find({"url": url}))