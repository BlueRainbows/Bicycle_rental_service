from rest_framework import serializers

from bicycle.models import Bicycle, Rental, Refunds
from bicycle.validators import DateValidator


class BicycleDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для детального просмотра о велосипеде.
    """
    class Meta:
        model = Bicycle
        exclude = ('status',)


class BicycleListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для просмотра списка велосипедов.
    """
    class Meta:
        model = Bicycle
        fields = ('pk', 'name', 'price',)


class RentalSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для аренды.
    """

    class Meta:
        model = Rental
        fields = '__all__'
        validators = [
            DateValidator(rent_date='rent_date')
        ]


class RefundsSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для возврата.
    """
    amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Refunds
        fields = '__all__'
