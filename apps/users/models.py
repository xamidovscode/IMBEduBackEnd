from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from helpers import phone_validator
from apps.base.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The Email field must be set")

        phone = self.normalize_email(phone)
        user = self.model(email=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser, BaseModel):

    first_name = None
    last_name = None
    email = None

    full_name = models.CharField(
        max_length=255
    )
    phone = models.CharField(
        max_length=255,
        validators=[phone_validator],
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith("pbkdf2_sha256"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }
