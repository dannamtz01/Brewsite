from app.brewsite import app

def test_home():
    client = app.test_client()
    response = client.get("/home/")
    
    assert response.status_code == 200
    assert b"Danna Martinez" in response.data