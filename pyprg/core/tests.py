from rest_framework.test import RequestsClient


def test_apiroot():
    client = RequestsClient()
    response = client.get('http://localhost:8000/')
    assert response.status_code == 200
