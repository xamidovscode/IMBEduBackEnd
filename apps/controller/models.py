from django.db import models
from django_tenants.models import TenantMixin, DomainMixin



class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "tenants"


class Domain(DomainMixin):
    class Meta:
        db_table = "domains"
