from django.db import models


class TenantMixin(object):
    """
    This is a mixin to provide a shared database aproach to the project tables.
    """

    tenant = models.ForeignKey('Tenant')


class Tenant(models.Model):
    """
    This model represents a tenant instance.
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    active_until = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def is_active(self):
        return active_until is not None

    def activate(self, date):
        self.active_until = date
        self.save()

    def deactivate(self):
        self.active_until = None
        self.save()
