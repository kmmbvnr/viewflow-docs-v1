===========
Quick Start
===========


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


To create a new module add `ModuleMixin` to your `AppConfig` definision in `apps.py`

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

