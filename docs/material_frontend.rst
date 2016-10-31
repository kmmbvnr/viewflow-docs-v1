=================
Material Frontend
=================

Introduction
============

Material Frontend is the lightweight alternative to the django admin
allows to build big modular websites.

- Lightweight module extension of django application config
- Ready to use theme build with ``MaterialzeCSS``
- Autocollected site navigation menu
- Fast and smooth navigation with Turbolinks
- CRUD scatffolding build with django class based views
- Out of the box datatables integration.

 
Installation
============

Add `material.frontend` into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         'material',
         'material.frontend',
         ...
    )

Add frontend urls into global urlconf module at urls.py

.. code-block:: python

    from material.frontend import urls as frontend_urls

    urlpatterns = [
        ...
        url(r'', include(frontend_urls)),
    ]


Quick start
===========

To create a new module add `ModuleMixin` to your `AppConfig` definition in `apps.py`

.. code-block:: python

    from material.frontend.apps import ModuleMixin

    class Sales(ModuleMixin, AppConfig):
        name = 'sales'
        icon = '<i class="mdi-communication-quick-contacts-dialer"></i>'

The application have to have <app_module>/urls.py file, with
a single no-parametrized url with name='index', ex

.. code-block:: python

    urlpatterns = [
            url('^$', generic.TemplateView.as_view(template_name="sales/index.html"), name="index"),
    ]

All AppConfigs urls will be included into material.frontend.urls automatically under /<app_label>/ prefix
The AppConfig.label, used for the urls namespace.

The menu.html sample

.. code-block:: html

        <ul>
            <li><a href="{% url 'sales:index' %}">Dashboard</a></li>
            <li><a href="{% url 'sales:customers' %}">Customers</a></li>
            {% if perms.sales.can_add_lead %}<li><a href="{% url 'sales:leads' %}">Leads</a></li>{% endif %}
        </ul>


Examples
========

The live demo of the frontend is available at http://forms.viewflow.io/integration

Demo source code available at the `Github <https://github.com/viewflow/django-material/tree/master/demo/tests/integration>`_
        
License
=======

Material Frontend is distributed as part of `django-material` package under the terms of the `BSD3 license <https://github.com/viewflow/django-material/blob/master/LICENSE.txt>`_

  
Table of Contents
=================

.. toctree::
   :maxdepth: 2

   frontend_modules
   frontend_crud
