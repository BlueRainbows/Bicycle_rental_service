from django.urls import path

from bicycle.apps import BicycleConfig
from bicycle import views

app_name = BicycleConfig.name

urlpatterns = [
    # Создание велосипеда
    path('create/', views.BicycleCreate.as_view(), name='bicycle_create'),
    # Список доступных велосипедов
    path('list/', views.BicycleList.as_view(), name='bicycle_list'),
    # Список всех велосипедов
    path('list/all/', views.BicycleListAll.as_view(), name='bicycle_list_all'),
    # Детальная информация о велосипеде
    path('detail/<int:pk>/', views.BicycleDetail.as_view(), name='bicycle_detail'),
    # Изменение велосипеда
    path('update/<int:pk>/', views.BicycleUpdate.as_view(), name='bicycle_update'),
    # Удаление велосипеда
    path('delete/<int:pk>/', views.BicycleDelete.as_view(), name='bicycle_delete'),

    # Добавление аренды
    path('rental/create/', views.RentalCreate.as_view(), name='rental_create'),
    # Список аренды пользователя
    path('rental/list/', views.RentalListPersonal.as_view(), name='rental_list'),
    # Список всех аренд
    path('rental/list/all/', views.RentalListManager.as_view(), name='rental_list_all'),
    # Изменение условий аренды
    path('rental/update/<int:pk>/', views.RentalUpdate.as_view(), name='rental_update'),
    # Удаление аренды
    path('rental/delete/<int:pk>/', views.RentalDelete.as_view(), name='rental_delete'),

    # Оформление возврата
    path('refunds/close/<int:pk>/', views.RefundsClose.as_view(), name='refunds_close'),
    # Список возвратов
    path('refunds/list/', views.RefundsList.as_view(), name='refunds_list')
]
