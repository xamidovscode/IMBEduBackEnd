from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from . import serializers
from .. import models

class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = models.User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        print(self.request.path)

        return Response({
            'id': user.id,
            'username': user.username,
            'full_name': user.full_name,
            'phone': user.phone,
            'token': user.tokens(),
            'roles': user.roles.all().values("name"),
            'branches': user.branches.all().values("name"),

        })


class TestAPIView(APIView):
    queryset = models.User.objects.all()

    def get(self, request, *args, **kwargs):
        return Response({
            "success": True,
        })

