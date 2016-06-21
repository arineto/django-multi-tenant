from django.forms import ModelForm
from multi_tenant.models import Tenant


class TenantThemeForm(ModelForm):

    class Meta:
        model = Tenant
        fields = ('theme',)
