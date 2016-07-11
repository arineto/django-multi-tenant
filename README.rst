Django Multi-Tenant
===================

Esse projeto está sendo desenvolvido como produto do Trabalho de Graduação do aluno José de Arimatea Rocha Neto
para o curso de Ciência da Computação na Universidade Federal de Pernambuco.

**Aluno:** José de Arimatea Rocha Neto

**Orientador:** Vinícius Cardoso Garcia

**Trabalho:** Uma biblioteca Multi-Tenant para o framework Django (link_)


**OBS:** Um exemplo do uso da biblioteca pode ser encontrado aqui_.

.. _link: https://www.overleaf.com/read/pqrgmvswqnrd/
.. _aqui: https://github.com/arineto/django-multi-tenant-example/

Instruções de Instalação
------------------------

Para instalar a biblioteca para rodar o comando

.. code-block:: python

  pip install git+https://github.com/arineto/django-multi-tenant.git

Instruções de Uso
-----------------

Para utilizar a biblioteca basta adicioná-la no ``INSTALLED_APPS`` do seu projeto.

.. code-block:: python

  INSTALLED_APPS = [
      ...
      'multi_tenant',
  ]

Middlewares
~~~~~~~~~~~

Para utilizar os Middlewares fornecidos pela biblioteca para adicioná-los no ``MIDDLEWARE_CLASSES`` do seu projeto.

.. code-block:: python

  MIDDLEWARE_CLASSES = [
      ...
      'multi_tenant.middleware.SubdomainMiddleware',
      'multi_tenant.middleware.TenantMiddleware',
  ]

Context Processorts
~~~~~~~~~~~~~~~~~~~

Para utilizar os Context Processors fornecidos pela biblioteca para adicioná-los no ``context_processors`` do seu projeto.

.. code-block:: python

  'context_processors': [
      ...
      'multi_tenant.context_processors.subdomain',
      'multi_tenant.context_processors.tenant',
      'multi_tenant.context_processors.theme',
  ]

TenantModel
~~~~~~~~~~~

Para utilizar o ``TenantModel`` e criar modelos que serão compartilhados entre os Tenants, basta importá-lo e criar os novos modelos a partir do mesmo.

.. code-block:: python

  from multi_tenant.models import TenantModel

  class ItemExample(TenantModel):

      name = models.CharField(max_length=10)
      code = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add=True)

TenantRequiredMixin
~~~~~~~~~~~~~~~~~~~

Para utilizar o ``TenantRequiredMixin`` e restringir o acesso para suas views, basta importá-lo e criar suas views a partir do mesmo.

.. code-block:: python

  from multi_tenant.auth import TenantRequiredMixin
  from .models import ItemExample

  class ItemListView(TenantRequiredMixin, ListView):

      model = ItemExample

      def get_queryset(self):
          return ItemExample.objects.by_tenant(self.request.tenant)
