from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from . import serializers
from .. import models

from helpers.permissions import (
    IsPublisher,

)

class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = models.User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        if request.tenant.schema_name != 'public':
            serializer = self.get_serializer(data=request.data, instance=request.tenant)
            serializer.is_valid(raise_exception=True)

            user = serializer.validated_data["user"]

            return Response({
                'id': user.id,
                'username': user.username,
                'full_name': user.full_name,
                'phone': user.phone,
                'token': user.tokens(),
                'role': user.role.name if user.role else None,
            })
        else:

            return Response({
                'id': user.id,
                'username': user.username,
                'full_name': user.full_name,
                'phone': user.phone,
                'token': user.tokens(),
                'role': user.role.name if user.role else None,
            })


class TestAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    permission_classes = [IsPublisher]

    def create(self, request, *args, **kwargs):

        from apps.controller.models import Tenant, Domain
        from django_tenants.utils import schema_context

        with schema_context("public"):
            Tenant.objects.create(
                schema_name='tests',
                name="test",
            )

        return Response({"success": True})



