from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import PermissionUser
from users.serializers import UserSerializer, UserCreateSerializer


class UserCreateView(CreateAPIView):
    """
    Создание нового пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Просмотр, редактирование и удаление пользователя.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & PermissionUser]

    def perform_update(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(serializer.validated_data['password'])
        user.save()

