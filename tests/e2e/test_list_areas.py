import requests

BASE_URL = "http://localhost:5000"


def test_list_areas_returns_200():
    response = requests.get(f"{BASE_URL}/areas")

    assert response.status_code == 200
