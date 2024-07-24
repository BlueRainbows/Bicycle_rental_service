# Generated by Django 5.0.4 on 2024-07-23 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Модель велосипеда')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Цена аренды велосипеда')),
                ('description', models.CharField(max_length=300, verbose_name='Характеристики велосипеда')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет велосипеда')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Доступен'), (1, 'Не доступен')], default=0, verbose_name='Статус доступности')),
            ],
            options={
                'verbose_name': 'Велосипед',
                'verbose_name_plural': 'Велосипеды',
            },
        ),
        migrations.CreateModel(
            name='Refunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_recall', models.DateField(blank=True, null=True, verbose_name='Дата последнего пересчёта суммы')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма возврата')),
                ('rent_status', models.BooleanField(default=True, verbose_name='Статус аренды')),
                ('refund_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
            ],
            options={
                'verbose_name': 'Возврат велосипеда',
                'verbose_name_plural': 'Возврат велосипедов',
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(verbose_name='Дата начала аренды')),
                ('bicycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bicycle.bicycle', verbose_name='Арендованный велосипед')),
            ],
            options={
                'verbose_name': 'Аренда велосипеда',
                'verbose_name_plural': 'Арендa велосипедов',
                'ordering': ['-rent_date'],
            },
        ),
    ]
