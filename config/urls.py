"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular import views

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Django users
    path('', include('users.urls', namespace='users')),
    # Django bicycles
    path('bicycles/', include('bicycle.urls', namespace='bicycle')),
    # drf-spectacular API docs
    path('api/schema/', views.SpectacularAPIView.as_view(), name='schema'),
    # Просмотр через Swagger и Redoc
    path('swagger-ui/', views.SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', views.SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
