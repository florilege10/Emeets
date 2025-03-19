from rest_framework import permissions

from Api_meets.models import User
from Api_meets.serializers import UserSerializer

class IsMan(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.sexe == 'H'

class IsWoman(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.sexe == 'F'
    
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

