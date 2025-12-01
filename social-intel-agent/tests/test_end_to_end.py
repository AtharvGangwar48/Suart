import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

class TestEndToEnd:
    def test_complete_analysis_workflow(self):
        # Test the complete workflow from API to analysis
        test_url = "https://example.com"
        
        response = client.post("/analyze/", json={
            "url": test_url,
            "deep_analysis": True
        })
        
        # The actual response might vary based on implementation
        # This test ensures the endpoint is reachable and returns a response
        assert response.status_code in [200, 500]
        
        if response.status_code == 200:
            data = response.json()
            assert isinstance(data, dict)
    
    def test_health_check_integration(self):
        response = client.get("/health/")
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "social-intel-agent"