from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import (
    Tenant,
    Domain,

)

@admin.register(Tenant)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('schema_name', 'name', )


@admin.register(Domain)
class DomainAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('tenant__schema_name', 'domain', )


