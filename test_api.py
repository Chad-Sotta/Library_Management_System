import pytest
from application import app

@pytest.fixture
def client():
    """Configures a test client workspace for executing runtime test routes."""
    app.config['TESTING'] = True
    
    # FORCE FLASK TO LOAD THE ROUTES FOR THE TEST SESSION
    with app.app_context():
        from application import routes
        
    with app.test_client() as client:
        yield client

def test_get_all_announcements(client):
    """Test standard retrieval of active system entries."""
    response = client.get('/api/announcements')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 1

def test_create_announcement_success(client):
    """Test structural inclusion validation via a successful POST sequence."""
    payload = {
        "title": "Renovation Notice",
        "content": "The West Wing study room will be closed for maintenance."
    }
    response = client.post('/api/announcements', json=payload)
    assert response.status_code == 201
    assert response.json["title"] == "Renovation Notice"

def test_create_announcement_missing_fields(client):
    """Test validation limits when processing malformed request bodies."""
    payload = {"title": "Incomplete Payload"}
    response = client.post('/api/announcements', json=payload)
    assert response.status_code == 400
    assert "error" in response.json

def test_get_announcement_not_found(client):
    """Test 404 boundary triggers with missing record ID parameters."""
    response = client.get('/api/announcements/9999')
    assert response.status_code == 404