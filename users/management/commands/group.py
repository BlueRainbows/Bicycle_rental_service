from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand
from bicycle.models import Bicycle, Rental, Refunds


class Command(BaseCommand):

    def handle(self, *args, **options):
        bicycle_perm = ContentType.objects.get_for_model(Bicycle)
        rental_perm = ContentType.objects.get_for_model(Rental)
        refunds_perm = ContentType.objects.get_for_model(Refunds)
        perm = [
            {'codename': 'add_bicycle', 'content_type': bicycle_perm},
            {'codename': 'change_bicycle', 'content_type': bicycle_perm},
            {'codename': 'view_bicycle', 'content_type': bicycle_perm},
            {'codename': 'delete_bicycle', 'content_type': bicycle_perm},
            {'codename': 'view_rental', 'content_type': rental_perm},
            {'codename': 'delete_rental', 'content_type': rental_perm},
            {'codename': 'view_refunds', 'content_type': refunds_perm}
        ]
        new_group = Group.objects.create(name='moderator_rentals')
        for p in perm:
            permission = Permission.objects.get(**p)
            new_group.permissions.add(permission)