from app import app


def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Welcome to ML Ops Assignment 1" in response.data
