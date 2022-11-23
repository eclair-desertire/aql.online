from rest_framework.permissions import BasePermission
from .models import User

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role==User.SUPERADMIN


class IsCourseOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.role==User.COURSEOWNER


class IsRegular(BasePermission):
    def has_permission(self, request, view):
        return request.user.role==User.REGULAR

