from rest_framework import permissions


class PermissionModer(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.groups.filter(name='moderator_rentals').exists():
            return True
        else:
            return False


class PermissionTenant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.tenant == request.user:
            return True
        return False


class PermissionUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.pk == request.user.pk:
            return True
        return False
