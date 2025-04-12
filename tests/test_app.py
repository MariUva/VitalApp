# tests/test_app.py
import sys
import os
import pytest

# Añade el directorio actual (donde está app.py) al path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    
    assert "<h1>VitalApp</h1>" in html
    assert "Bienvenido a tu clínica en línea" in html
    assert "Agendar Cita" in html
    assert "Examen de sangre" in html
    assert "Rayos X" in html
    assert "Salud Vital" in html