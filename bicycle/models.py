from django.db import models

from users.models import User

CHOICE_RENTAL = [
    (0, 'Доступен'),
    (1, 'Не доступен'),
]


class Bicycle(models.Model):
    """
    Модель велосипеда.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Модель велосипеда"
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Цена аренды велосипеда",
        default=0,
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Характеристики велосипеда"
    )
    color = models.CharField(
        max_length=50,
        verbose_name="Цвет велосипеда"
    )
    status = models.PositiveSmallIntegerField(
        choices=CHOICE_RENTAL,
        verbose_name="Статус доступности",
        default=0,
    )

    def __str__(self):
        return f'{self.name}, цвет {self.color}, цена аренды {self.price}'

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"


class Rental(models.Model):
    """
    Модель аренды велосипеда.
    """
    tenant = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Арендатор",
        null=True,
        blank=True
    )
    bicycle = models.ForeignKey(
        Bicycle, on_delete=models.CASCADE,
        verbose_name="Арендованный велосипед"
    )
    rent_date = models.DateField(
        verbose_name="Дата начала аренды",
    )

    def __str__(self):
        return f'Аренда велосипеда {self.bicycle}, пользователем {self.tenant}'

    class Meta:
        verbose_name = "Аренда велосипеда"
        verbose_name_plural = "Арендa велосипедов"
        ordering = ['-rent_date']


class Refunds(models.Model):
    """
    Модель возврата велосипеда.
    """
    rental = models.ForeignKey(
        Rental, on_delete=models.CASCADE,
        verbose_name="Аренда велосипеда"
    )
    last_recall = models.DateField(
        verbose_name="Дата последнего пересчёта суммы",
        null=True,
        blank=True
    )
    amount = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма возврата"
    )
    rent_status = models.BooleanField(
        verbose_name="Статус аренды",
        default=True
    )
    refund_date = models.DateField(
        verbose_name="Дата возврата",
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Возврат аренды'

    class Meta:
        verbose_name = "Возврат велосипеда"
        verbose_name_plural = "Возврат велосипедов"
