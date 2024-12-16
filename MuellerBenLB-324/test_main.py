import pytest
from main import app  # Importiere die Flask-App aus der 'main.py'-Datei

@pytest.fixture
def client():
    # Diese Fixture stellt einen Test-Client für die Flask-App zur Verfügung
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Teste die Startseite
    response = client.get('/')
    
    # Überprüfe, ob der HTTP-Statuscode 200 zurückgegeben wird
    assert response.status_code == 200

    # Überprüfe, ob der Text 'Willkomme! Gib dä Name ii:' im Antworttext enthalten ist
    assert b"Willkomme! Gib de Name ii:" in response.data  # Achte darauf, dass dies ein Byte-String ist

    # Überprüfe, ob der Text 'Abschicke' im Antworttext enthalten ist
    assert b"Abschicke" in response.data
