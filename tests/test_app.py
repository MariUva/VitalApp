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

    html = response.data.decode('utf-8').lower()  # Lo pasamos a minúsculas para facilitar las comparaciones

    # Verificamos que el contenido esperado esté presente en el HTML
    assert "vitalapp" in html
    assert "bienvenido a tu clínica en línea" in html
    assert "agendar cita" in html
    assert "examen de sangre" in html
    assert "rayos x" in html
    assert "salud vital" in html
