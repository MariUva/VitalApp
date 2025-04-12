import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"VitalApp" in response.data  # Ajusta esto según tu HTML
