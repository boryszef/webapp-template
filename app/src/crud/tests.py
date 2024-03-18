"""
Tests for sample app views
"""

from unittest.mock import patch
import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from crud.tasks import recompute_weights
from crud.models import Data


@pytest.mark.django_db
def test_get_list():
    """
    Test if view returns a full list of items
    """
    baker.make('crud.Data')
    baker.make('crud.Data')
    client = APIClient()
    response = client.get(
        reverse('data-list')
    )
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_get_specific():
    """
    Test if view returns the given item
    """
    item = baker.make('crud.Data')
    client = APIClient()
    response = client.get(
        reverse('data-detail', kwargs={'pk': item.id})
    )
    assert response.status_code == 200
    assert response.json()['name'] == item.name


@pytest.mark.django_db
def test_create_instance():
    """
    Test creation of an item
    """
    name = 'foobar'
    client = APIClient()
    response = client.post(
        reverse('data-list'),
        {'name': name, 'value': 13},
        format='json'
    )
    assert response.status_code == 201
    item = response.json()
    assert Data.objects.get(pk=item['id']).name == name


@pytest.mark.django_db
def test_delete_instance():
    """
    DELETE request should remove the instance
    """
    item = baker.make('crud.Data')
    client = APIClient()
    response = client.delete(
        reverse('data-detail', kwargs={'pk': item.id})
    )
    assert response.status_code == 204
    with pytest.raises(ObjectDoesNotExist):
        Data.objects.get(pk=item.id)


@pytest.mark.django_db
def test_recompute_weights():
    """
    Test that recomputed weights are correct
    """
    one = baker.make('crud.Data', value=1)
    nine = baker.make('crud.Data', value=9)
    recompute_weights()
    assert Data.objects.get(pk=one.id).weight == pytest.approx(0.1)
    assert Data.objects.get(pk=nine.id).weight == pytest.approx(0.9)


@pytest.mark.django_db
@patch('crud.listeners.recompute_weights')
def test_post_triggers_recompute(mock_recompute):
    """
    post_save signal should trigger the task
    """
    client = APIClient()
    for _ in range(3):
        client.post(
            reverse('data-list'),
            {'name': 'foo', 'value': 13},
            format='json'
        )
    assert len(mock_recompute.delay.mock_calls) == 3


@pytest.mark.django_db
@patch('crud.listeners.recompute_weights')
def test_delete_triggers_recompute(mock_recompute):
    """
    post_delete signal should trigger the task
    """
    assert len(mock_recompute.delay.mock_calls) == 0
    item = baker.make('crud.Data')
    client = APIClient()
    client.post(
        reverse('data-detail', kwargs={'pk': item.id})
    )
    assert len(mock_recompute.delay.mock_calls) == 1
