import pytest

from rest_framework.test import APIClient
from users.models import User


@pytest.fixture
def user():
    return User.objects.create(
        first_name='Test',
        email='Test@testow.ru',
        password='testpassword'
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_client(user, api_client):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
