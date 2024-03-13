"""
Basic tests to check if django works
"""

from django.test import Client


def test_response():
    """
    Should redirect to login page (code 302)
    """
    response = Client().get("/admin/")
    assert response.status_code == 302
