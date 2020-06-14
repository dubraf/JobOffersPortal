from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsEmployer(permissions.BasePermission):
    message = 'Only employer can add job offers and its content'

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.isEmployer

class IsOwner(permissions.BasePermission):
    message = 'Only owner can modify this content'

    def has_object_permission(self, request, view, obj) :
        if request.method in permissions.SAFE_METHODS :
            return True
        return request.user.user_id == obj.user_id