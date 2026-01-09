from fastapi.testclient import TestClient

from fastapi_zero.app import app

def test_root_deve_retornar_ola_mundo():
    """
    AAA
    A - Arrange - Prepara
    A - Act - Age
    A - Assert - Garante
    """
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
