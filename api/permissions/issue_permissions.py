from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsReportingStudentOrStaff(permissions.BasePermission):
    """
    Student can view their own records
    Staff can view all
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.groups.exclude(name='Student').exists():
            return True
        return bool(obj.student == request.user)


class IsStaff(permissions.BasePermission):
    """
    Ensures user has any group other than staff
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.groups.exclude(name='Student').exists())

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Allows Read/Write to Staff, Read-only to Students
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.groups.exclude(name='Student').exists()
            )


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
            (request.user and
            request.user.groups.filter(name='Admin'))
        )
