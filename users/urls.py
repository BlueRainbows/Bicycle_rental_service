from django.urls import path
from rest_framework import permissions

from users.apps import UsersConfig
from users import views
from rest_framework_simplejwt import views as jwt

app_name = UsersConfig.name

urlpatterns = [
    # Вход в систему
    path('', jwt.TokenObtainPairView.as_view(permission_classes=(permissions.AllowAny,)), name='login'),
    # Регистрация
    path('register/', views.UserCreateView.as_view(permission_classes=(permissions.AllowAny,)), name='register'),
    # Получение токена
    path('token/refresh/', jwt.TokenRefreshView.as_view(permission_classes=(permissions.AllowAny,)), name='token_refresh'),
    # Взаимодействие с профилем
    path('profile/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='profile'),
]
