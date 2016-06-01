from django.db import models
from multi_tenant.models import TenantModel


class Item(TenantModel):

    name = models.CharField(max_length=10)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
