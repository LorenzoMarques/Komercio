from rest_framework import permissions

class ProductCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
          request.user.is_authenticated and request.user.is_seller
        )

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.seller_id == request.user.id:
            return True