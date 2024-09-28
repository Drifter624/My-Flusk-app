# tests/test_app.py
import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'¡Hola, mundo! Esta es una aplicación Flask.'
