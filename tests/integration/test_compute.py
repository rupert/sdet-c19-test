import json

import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_compute_returns_200(client):
    response = client.post(
        "/compute",
        data=json.dumps(
            {
                "sample": 2000,
                "area_code": "E92000001",
            }
        ),
    )

    assert response.status_code == 200
