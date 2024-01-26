from rest_framework import permissions


class IsAuthenticatedOrReadOnlyForPost(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS or
            obj.published or
            request.user.is_authenticated
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return (
            request.method in permissions.SAFE_METHODS or
            obj.user == request.user or
            request.user.is_superuser
        )
