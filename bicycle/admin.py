from django.contrib import admin

from bicycle.models import Bicycle, Rental, Refunds


@admin.register(Bicycle)
class BicycleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    list_filter = ('status',)


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'bicycle', 'rent_date',)
    list_filter = ('rent_date',)
    list_display_links = ['tenant', 'bicycle']


@admin.register(Refunds)
class RefundsAdmin(admin.ModelAdmin):
    list_display = ('id', 'rent_status', 'rental', 'amount', 'refund_date', )
    list_filter = ('refund_date', 'rent_status',)
    list_display_links = ['rental']
