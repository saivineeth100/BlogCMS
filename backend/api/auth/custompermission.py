
from rest_framework import permissions
from users.models import UserRoles

class IsAdmin(permissions.BasePermission):
    message = 'User must be Admin or Super Admin'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        usertype = request.user.user_role
        isadmin = usertype == UserRoles.ADMIN or usertype == UserRoles.SUPERADMIN
        return isadmin