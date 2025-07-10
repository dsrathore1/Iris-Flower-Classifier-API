from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "All running good!"


def test_predict_valid():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert response.json()["prediction"] in ["setosa", "versicolor", "virginica"]


def test_predict_invalid_short_input():
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 422
    assert "message" in response.json() or "detail" in response.json()


def test_predict_missing_input():
    response = client.post("/predict", json={})
    assert response.status_code == 422
