from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from multi_tenant.exceptions import IncorrectTenantException
from multi_tenant.auth import belongs_to_tenant
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


class LoginView(View):

    template_name = 'example/login.html'

    def get(self, request):
        return render_to_response(self.template_name, RequestContext(request))

    def post(self, request, *args, **kwargs):
        context = RequestContext(request)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            if request.tenant:
                belongs_to_tenant(username, request.tenant)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = 'Login realizado com sucesso.'
                else:
                    mssage = 'Usuário inativo.'
            else:
                message = 'Usuário ou senha incorretos.'
        except IncorrectTenantException:
            message = 'Usuário não registrado para o Tenant.'

        context['message'] = message
        return render_to_response(self.template_name, context)


class LogoutView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return reverse_lazy('example:login')


class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'code']
    success_url = 'example:list_item'
