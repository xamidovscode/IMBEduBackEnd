from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .. import models




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = models.User.objects.filter(username=username).first()

        if not user:
            raise serializers.ValidationError(
                {"username": _("User not found")}
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                {"password": _("Password is incorrect")}
            )

        return {"user": user}



