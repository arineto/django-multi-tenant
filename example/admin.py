from django.contrib import admin
from .models import Item
from multi_tenant.models import Theme
from multi_tenant.models import Tenant

# Register your models here.
admin.site.register(Item)
admin.site.register(Theme)
admin.site.register(Tenant)
