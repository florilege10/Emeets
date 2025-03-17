from rest_framework import permissions

class IsMan(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.sexe == 'H'

class IsWoman(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.sexe == 'F'