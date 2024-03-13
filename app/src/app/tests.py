from django.test import Client


def test_response():
    response = Client().get("/admin/")
    assert response.status_code == 302