from rest_framework.permissions import BasePermission, SAFE_METHODS

class MasterPermission(BasePermission):
    message = 'You do not have the permission to access this view'
    def has_permission(self, request, view):
        return request.user.roles == 'master'


class UserEditDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        message = 'You do not have the permission to edit the details of this object'
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
