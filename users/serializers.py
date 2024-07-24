from rest_framework import serializers

from bicycle.models import Refunds
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)

    def get_history(self, obj):
        return (f"Всего вы сделали {Refunds.objects.filter(rental__tenant=obj).count()} аренд. "
                f"Колличество завершенных аренд: "
                f"{Refunds.objects.filter(rental__tenant=obj).filter(rent_status=False).count()}")

    def get_amount(self, obj):
        summ = 0
        for refund in Refunds.objects.filter(rental__tenant=obj).filter(rent_status=True):
            summ += refund.amount
        return f"Сумма за текущие аренды: {summ}"

    class Meta:
        model = User
        fields = ('first_name', 'email', 'history', 'amount', 'password')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')
