from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True


class IsSuperUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj)
        if request.user.is_superuser:
            return True