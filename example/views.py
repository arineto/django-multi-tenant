from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from multi_tenant.models import Tenant
from .models import Item
from .forms import TenantThemeForm


class HomeView(TemplateView):
    template_name = 'example/home.html'


class SubdomainView(TemplateView):
    template_name = 'example/subdomain.html'


class ItemListView(ListView):
    model = Item
    paginate_by = 20

    def get_queryset(self):
        return Item.objects.by_tenant(self.request.tenant)


class ThemeUpdateView(UpdateView):
    model = Tenant
    form_class = TenantThemeForm
    template_name = 'example/tenant_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'example:tenant_theme', args=(self.request.tenant.pk,)
        )


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'code']
    success_url = 'example:list_item'
