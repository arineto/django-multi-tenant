from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^subdomain/$', views.SubdomainView.as_view(), name='subdomain'),
    url(r'^list_items/$', views.ItemListView.as_view(), name='list_items'),
    url(r'^tenant_theme/(?P<pk>\d+)/$', views.ThemeUpdateView.as_view(),
        name='tenant_theme'),
    url(r'^create_item/$', views.ItemCreateView.as_view(), name='create_item'),
]
