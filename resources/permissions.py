from rest_framework.permissions import BasePermission, SAFE_METHODS

class MasterPermission(BasePermission):
    message = 'You do not have the permission to access this view'
    def has_permission(self, request, view):
        return request.user.roles == 'master'

class WorkerPermission(BasePermission):
    message = 'You do not have the permission to access this view'
    def has_permission(self, request, view):
        return request.user.roles == 'worker'


class UserEditDeletePermission(BasePermission):
    message = 'You do not have the permission to edit the details of this object'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
