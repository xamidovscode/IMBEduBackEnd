from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework import HTTP_HEADER_ENCODING
from django.apps import apps
from django.db import connection

def get_dynamic_user_model():
    schema = connection.schema_name
    print(schema, 111111111111111)

    if schema == 'public':
        return apps.get_model('controller', 'User')
    else:
        return apps.get_model('users', 'User')


class CustomJWTAuthentication(BaseAuthentication):
    """
    Custom JWT Authentication class that does not rely on api_settings for header type/name.
    """

    www_authenticate_realm = 'api'
    AUTH_HEADER_TYPE = b'Bearer'
    AUTH_HEADER_NAME = 'HTTP_AUTHORIZATION'

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        return (user, validated_token)

    def get_header(self, request):
        auth = request.META.get(self.AUTH_HEADER_NAME, b'')
        if isinstance(auth, str):
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth

    def get_raw_token(self, header):
        parts = header.split()

        if len(parts) == 0:
            return None

        if parts[0].lower() != self.AUTH_HEADER_TYPE.lower():
            return None

        if len(parts) == 1:
            return None

        if len(parts) > 2:
            return None

        return parts[1]

    def get_validated_token(self, raw_token):
        try:
            return UntypedToken(raw_token)
        except Exception as e:
            raise InvalidToken(f"Token is invalid or expired: {str(e)}")

    def get_user(self, validated_token):
        UserModel = get_dynamic_user_model()
        user_id = validated_token.get('user_id')

        if user_id is None:
            raise AuthenticationFailed('Token contained no recognizable user identification')

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            raise AuthenticationFailed('User not found')

        if not user.is_active:
            raise AuthenticationFailed('User is inactive')

        return user

    def authenticate_header(self, request):
        return f'{self.AUTH_HEADER_TYPE.decode()} realm="{self.www_authenticate_realm}"'
