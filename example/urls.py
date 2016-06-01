from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ItemListView.as_view(), name='list_item'),
    url(r'^create/$', views.ItemCreateView.as_view(), name='create_item'),
]
