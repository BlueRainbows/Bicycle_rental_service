from datetime import datetime

import pytest

from bicycle.models import Bicycle, Rental, Refunds
from users.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    """ Фикстура на пользователя """
    return User.objects.create(
        first_name='Test',
        email='Test@testow.ru',
        password='testpassword'
    )


@pytest.fixture
def admin():
    """ Фикстура на админа """
    return User.objects.create(
        first_name='Admin',
        email='Admin@adminow.ru',
        password='adminpassword',
        is_superuser=True,
        is_staff=True
    )


@pytest.fixture
def api_client():
    """ Фикстура получения клиента """
    return APIClient()


@pytest.fixture
def authenticated_admin(admin, api_client):
    """ Фикстура на авторизацию админа """
    api_client.force_authenticate(user=admin)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def authenticated_client(user, api_client):
    """ Фикстура на авторизацию пользователя """
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture
def bicycle():
    """ Фикстура на велосипед """
    return Bicycle.objects.create(
        name='BmV 600',
        description='Скоростной велосипед',
        price=500,
        color='Черный'
    )


@pytest.fixture
def rental(bicycle, user):
    """ Фикстура на аренду """
    return Rental.objects.create(
        tenant=user,
        bicycle=bicycle,
        rent_date=datetime.now().date(),
    )


@pytest.fixture
def refunds(rental):
    """ Фикстура на аренду """
    return Refunds.objects.create(
        rental=rental
    )
