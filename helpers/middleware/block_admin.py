from django.http import HttpResponseForbidden
from django.db import connection

class BlockAdminInPublicSchemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and connection.schema_name == 'public':
            return HttpResponseForbidden("")
        return self.get_response(request)



