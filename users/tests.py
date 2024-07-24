from django.urls import reverse
from rest_framework import status
from users.fixtures import *

from users.models import User


@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('users:register')
    data = {'first_name': 'Test1', 'email': 'Test1@testow.ru', 'password': 'newpassword'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email='Test1@testow.ru').exists()


@pytest.mark.django_db
def test_get_user_data(authenticated_client, user):
    url = reverse('users:profile', kwargs={'pk': user.pk})
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['email'] == user.email

    data = {'first_name': 'PatchTest', 'email': user.email, 'password': user.password}
    response = authenticated_client.patch(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['first_name'] == 'PatchTest'

    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert User.objects.filter(email=user.email).exists() == False
