"""
Tests for sample app views
"""

from django.urls import reverse
from rest_framework.test import APIClient

from crud.models import Data


def test_get_list():
    """
    Test if view returns a full list of items
    """
    Data.objects.create([
        Data(name='foo', value=1),
        Data(name='bar', value=2)
    ])
    client = APIClient()
    response = client.get(
        reverse('data-list')
    )
    assert response.status_code == 200



def test_get_specific():
    """
    Test if view returns the given item
    """


def test_create_instance():
    """
    Test creation of an item
    """
