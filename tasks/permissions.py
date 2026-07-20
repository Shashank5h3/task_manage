from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    """
    Admin users can access all tasks.
    Regular users can access only their own tasks.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.groups.filter(name="Admin").exists():
            return True

        return obj.owner == request.user