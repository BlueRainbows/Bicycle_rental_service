from datetime import datetime, timedelta

from django.urls import reverse
from rest_framework import status
from bicycle.fixtures import *


@pytest.mark.django_db
def test_create_bicycle_user(authenticated_client):
    """ Тест на создание велосипеда пользователем """
    url = reverse('bicycle:bicycle_create')
    data = {'name': 'Velosiped',
            'price': '200',
            'description': 'High-speed bike',
            'color': 'Blue'}
    response = authenticated_client.post(url, data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_bicycle_admin(authenticated_admin):
    """ Тест на создание велосипеда админом """
    url = reverse('bicycle:bicycle_create')
    data = {'name': 'Velosiped',
            'price': '200',
            'description': 'High-speed bike',
            'color': 'Blue'}
    response = authenticated_admin.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_list_bicycle_user(authenticated_client):
    """ Тест на просмотр списка велосипеда пользователем """
    url = reverse('bicycle:bicycle_list')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    url = reverse('bicycle:bicycle_list_all')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_list_bicycle_admin(authenticated_admin):
    """ Тест на просмотр списка велосипеда админом """
    url = reverse('bicycle:bicycle_list')
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK
    url = reverse('bicycle:bicycle_list_all')
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_content_bicycle_user(authenticated_client, bicycle):
    """ Тест на управление контентом велосипеда пользователем """
    url = reverse('bicycle:bicycle_detail', kwargs={'pk': bicycle.pk})
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == bicycle.name
    url = reverse('bicycle:bicycle_update', kwargs={'pk': bicycle.pk})
    response = authenticated_client.patch(url, data={'name': 'BMV 600'})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    url = reverse('bicycle:bicycle_delete', kwargs={'pk': bicycle.pk})
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_content_bicycle_admin(authenticated_admin, bicycle):
    """ Тест на управление контентом велосипеда админом """
    url = reverse('bicycle:bicycle_detail', kwargs={'pk': bicycle.pk})
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == bicycle.name
    url = reverse('bicycle:bicycle_update', kwargs={'pk': bicycle.pk})
    response = authenticated_admin.patch(url, data={'name': 'BMV 600'})
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'BMV 600'
    url = reverse('bicycle:bicycle_delete', kwargs={'pk': bicycle.pk})
    response = authenticated_admin.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_rental_create(authenticated_client, bicycle):
    """ Тест на создание аренды """
    url = reverse('bicycle:rental_create')
    response = authenticated_client.post(url, data={
        'bicycle': bicycle.pk,
        'rent_date': datetime.now().date() + timedelta(days=40)})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = authenticated_client.post(url, data={
        'bicycle': bicycle.pk,
        'rent_date': datetime.now().date() - timedelta(days=1)})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = authenticated_client.post(url, data={
        'bicycle': bicycle.pk,
        'rent_date': datetime.now().date()})
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_list_rental_user(authenticated_client):
    """ Тест на просмотр списка аренды пользователем """
    url = reverse('bicycle:rental_list')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    url = reverse('bicycle:rental_list_all')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_list_rental_admin(authenticated_admin):
    """ Тест на просмотр списка аренды админом """
    url = reverse('bicycle:rental_list')
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK
    url = reverse('bicycle:rental_list_all')
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_content_rental_user(authenticated_client, rental, bicycle):
    """ Тест на управление контентом аренды пользователем """
    url = reverse('bicycle:rental_update', kwargs={'pk': rental.pk})
    response = authenticated_client.patch(url, data={
        'rent_date': datetime.now().date() + timedelta(days=1)})
    assert response.status_code == status.HTTP_200_OK
    dates = datetime.now().date() + timedelta(days=1)
    assert response.data['rent_date'] == str(dates)
    url = reverse('bicycle:rental_delete', kwargs={'pk': rental.pk})
    response = authenticated_client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_content_rental_admin(authenticated_admin, rental, bicycle):
    """ Тест на управление контентом аренды админом """
    url = reverse('bicycle:rental_update', kwargs={'pk': rental.pk})
    response = authenticated_admin.patch(url, data={
        'rent_date': datetime.now().date() + timedelta(days=1)})
    assert response.status_code == status.HTTP_200_OK
    dates = datetime.now().date() + timedelta(days=1)
    assert response.data['rent_date'] == str(dates)
    url = reverse('bicycle:rental_delete', kwargs={'pk': rental.pk})
    response = authenticated_admin.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_refunds_admin(authenticated_client, refunds):
    """ Тест на управление контентом возврата и списком у пользователя """
    url = reverse('bicycle:refunds_close', kwargs={'pk': refunds.pk})
    response = authenticated_client.patch(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    url = reverse('bicycle:refunds_list')
    response = authenticated_client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_refunds_admin(authenticated_admin, refunds):
    """ Тест на управление контентом возврата и списком у админа """
    url = reverse('bicycle:refunds_close', kwargs={'pk': refunds.pk})
    response = authenticated_admin.patch(url)
    assert response.status_code == status.HTTP_200_OK
    url = reverse('bicycle:refunds_list')
    response = authenticated_admin.get(url)
    assert response.status_code == status.HTTP_200_OK
