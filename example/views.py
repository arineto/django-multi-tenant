from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Item


class ItemListView(ListView):
    model = Item


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'code']
    success_url = 'example:list_item'
