from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from helpers import phone_validator
from apps.common.models import BaseModel, Branch


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Email field must be set")

        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser, BaseModel):

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
    role = models.ForeignKey(
        'users.Role',
        on_delete=models.PROTECT,
        related_name='users',
        null=True, blank=True,
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


class UserBranch(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_branches",
    )
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='user_branches',
    )

    class Meta:
        unique_together = ('user', 'branch')



