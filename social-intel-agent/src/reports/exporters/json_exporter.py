import json
from datetime import datetime

class JSONExporter:
    def export_to_json(self, report_data: dict) -> str:
        # Ensure all datetime objects are serializable
        serializable_data = self._make_serializable(report_data)
        
        return json.dumps(serializable_data, indent=2, ensure_ascii=False)
    
    def _make_serializable(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, dict):
            return {key: self._make_serializable(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        else:
            return obj
    
    def save_to_file(self, report_data: dict, filename: str):
        json_content = self.export_to_json(report_data)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_content)
        
        return filename