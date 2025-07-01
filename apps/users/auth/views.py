from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from . import serializers
from .. import models

from helpers.permissions import (
    IsPublisher, IsPublic,

)

class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = models.User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, instance=request.tenant)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        return Response({
            'id': user.id,
            'token': user.tokens(),
        })



class TestAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    permission_classes = [IsPublic]

    def create(self, request, *args, **kwargs):

        return Response({"success": True})



