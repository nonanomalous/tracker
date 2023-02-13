from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsReportingStudentOrAdmin(permissions.BasePermission):
    """
    Student can view their own records
    Admin can view all
    """
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.groups.filter(name='Admin'):
            return True
        return bool(obj.student == request.user)

class IsAdmin(permissions.BasePermission):
    """
    Admin only
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.groups.filter(name='Admin')
        )

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Admin or read only
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.groups.filter(name='Admin')
        )