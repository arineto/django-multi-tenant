from django.db import models


class TenantModelManager(models.Manager):
    """
    This manager makes it easy to filter by tenant
    """

    def by_tenant(self, tenant):
        return self.filter(tenant=tenant)

    def by_tenants(self, tenants):
        return self.filter(tenant__in=tenants)
