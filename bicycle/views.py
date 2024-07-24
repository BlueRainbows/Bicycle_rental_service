from datetime import datetime

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bicycle import serializers
from rest_framework import generics
from rest_framework.views import APIView

from bicycle.models import Bicycle, Rental, Refunds
from users.permissions import PermissionModer, PermissionTenant


################################################################################


class BicycleCreate(generics.CreateAPIView):
    """
    Создание велосипеда, доступ только у модератора/администратора.
    """
    queryset = Bicycle.objects.all()
    serializer_class = serializers.BicycleDetailSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


class BicycleList(generics.ListAPIView):
    """
    Список доступных велосипедов, виден всем пользователям.
    """
    queryset = Bicycle.objects.filter(status=0)
    serializer_class = serializers.BicycleListSerializer


class BicycleListAll(generics.ListAPIView):
    """
    Список всех велосипедов, доступен только у модератора/администратора.
    """
    queryset = Bicycle.objects.all()
    serializer_class = serializers.BicycleListSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


class BicycleDetail(generics.RetrieveAPIView):
    """
    Просмотр информации о велосипеде.
    """
    queryset = Bicycle.objects.all()
    serializer_class = serializers.BicycleDetailSerializer


class BicycleUpdate(generics.UpdateAPIView):
    """
    Изменение информации о велосипеде, доступ только у модератора/администратора.
    """
    queryset = Bicycle.objects.all()
    serializer_class = serializers.BicycleDetailSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


class BicycleDelete(generics.DestroyAPIView):
    """
    Удаление велосипеда, доступ только у модератора/администратора.
    """
    queryset = Bicycle.objects.all()
    serializer_class = serializers.BicycleListSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


################################################################################


class RentalCreate(generics.CreateAPIView):
    """
    Создание аренды велосипеда.
    """
    queryset = Rental.objects.all()
    serializer_class = serializers.RentalSerializer

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user)
        Bicycle.objects.filter(pk=self.request.data['bicycle']).update(status=1)


class RentalListPersonal(generics.ListCreateAPIView):
    """
    Список аренд велосипедов текущего пользователя.
    """
    queryset = Rental.objects.all()
    serializer_class = serializers.RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(tenant=self.request.user)


class RentalListManager(generics.ListCreateAPIView):
    """
    Список аренд велосипедов для модератора/администратора.
    """
    queryset = Rental.objects.all()
    serializer_class = serializers.RentalSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


class RentalUpdate(generics.UpdateAPIView):
    """
    Изменение аренды велосипеда.
    """
    queryset = Rental.objects.all()
    serializer_class = serializers.RentalSerializer
    permission_classes = [IsAuthenticated, PermissionModer | PermissionTenant]


class RentalDelete(generics.DestroyAPIView):
    """
    Удаление аренды велосипеда, доступ только у модератора/администратора.
    """
    queryset = Rental.objects.all()
    serializer_class = serializers.RentalSerializer
    permission_classes = [IsAuthenticated & PermissionModer]


################################################################################


class RefundsClose(APIView):
    """
    Закрытые аренды велосипеда, доступ только у модератора/администратора.
    """
    serializer_class = serializers.RefundsSerializer
    permission_classes = [IsAuthenticated & PermissionModer]

    def patch(self, request, pk):
        refund = get_object_or_404(Refunds, pk=pk)
        refund.rent_status = False
        refund.refund_date = datetime.now().date()
        Bicycle.objects.filter(pk=refund.rental.bicycle.pk).update(status=0)
        refund.save()
        message = (f'Возврат аренды велосипеда {refund.rental.bicycle.name} пользователем'
                   f' {refund.rental.tenant} был осуществлен. '
                   f'Итоговая сумма аренды {refund.amount} рублей.')
        return Response({"message": message}, status=200)


class RefundsList(generics.ListAPIView):
    """
    Список аренд велосипеда, доступ только у модератора/администратора.
    """
    queryset = Refunds.objects.all()
    serializer_class = serializers.RefundsSerializer
    permission_classes = [IsAuthenticated & PermissionModer]
