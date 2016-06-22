from django.contrib.auth.models import User
from django.db import models
from .managers import TenantModelManager


class Theme(models.Model):
    """
    This model stores all the available themes.
    """

    name = models.CharField(max_length=100, unique=True)
    stylesheets = models.FileField(upload_to='themes/')

    def __str__(self):
        return self.name


class Tenant(models.Model):
    """
    This model represents a tenant instance.
    """

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    active_until = models.DateField(null=True, blank=True)
    theme = models.ForeignKey(Theme, null=True, blank=True)
    users = models.ManyToManyField(User)

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


class TenantModel(models.Model):
    """
    This is a abstract model to provide a shared database aproach to the
    project tables.
    """

    tenant = models.ForeignKey(Tenant, related_name='tenant')
    objects = TenantModelManager()

    class Meta:
        abstract = True
