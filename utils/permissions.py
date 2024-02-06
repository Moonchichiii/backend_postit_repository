from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to only allow "owners" users of objects to edit 
    """

    def has_object_permission(self, request, view, obj):
        
        
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return obj.profile.user == request.user or request.user.is_superuser