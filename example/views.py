from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Item


class HomeView(TemplateView):
    template_name = 'example/home.html'


class SubdomainView(TemplateView):
    template_name = 'example/subdomain.html'


class ItemListView(ListView):
    model = Item
    paginate_by = 20

    def get_queryset(self):
        return Item.objects.by_tenant(self.request.tenant)


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'code']
    success_url = 'example:list_item'
