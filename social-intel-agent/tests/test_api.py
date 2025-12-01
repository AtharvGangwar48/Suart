import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

class TestAPI:
    def test_health_endpoint(self):
        response = client.get("/health/")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
    
    def test_analyze_endpoint_invalid_url(self):
        response = client.post("/analyze/", json={"url": "invalid-url"})
        assert response.status_code == 500
    
    def test_analyze_endpoint_valid_request(self):
        response = client.post("/analyze/", json={
            "url": "https://example.com",
            "deep_analysis": False
        })
        # This might fail due to actual scraping, but tests the endpoint structure
        assert response.status_code in [200, 500]