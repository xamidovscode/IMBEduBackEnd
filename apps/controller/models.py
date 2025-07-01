from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from rest_framework_simplejwt.tokens import RefreshToken



class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tenants"


class Domain(DomainMixin):
    class Meta:
        db_table = "domains"


from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    username = models.CharField(
        max_length=100,
        unique=True,
        help_text="Username must be unique."
    )
    password = models.CharField(
        max_length=128,
        help_text="Hashed password"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether this user is active"
    )

    def set_password(self, raw_password):
        """Hashes the password and stores it."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Checks if the provided raw password matches the hashed one."""
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # Only hash if not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }
