from django import forms
from multi_tenant.models import Tenant


class TenantThemeForm(forms.ModelForm):

    class Meta:
        model = Tenant
        fields = ('theme',)
