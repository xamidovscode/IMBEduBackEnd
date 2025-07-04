from rest_framework import permissions


class IsPublisher(permissions.BasePermission):

    def has_permission(self, request, view):
        path = "/api/v1/auth/test/"
        print(path, 11111)

        return (
            request.user.is_authenticated
            and
            request.path == path
        )


class IsPublic(permissions.BasePermission):

    def has_permission(self, request, view):

        return (
            request.user.is_active
            and
            request.tenant.schema_name == "public"
        )
