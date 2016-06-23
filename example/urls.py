from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^subdomain/$', views.SubdomainView.as_view(), name='subdomain'),
    url(r'^list_items/$', views.SimpleItemListView.as_view(),
        name='simple_list_items'),
    url(r'^tenant_list_items/$', views.RestrictedItemListView.as_view(),
        name='restricted_list_items'),
    url(r'^tenant_theme/(?P<pk>\d+)/$', views.ThemeUpdateView.as_view(),
        name='tenant_theme'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]
