==================
Material Dashboard
==================

Introduction
============

Material Dashboard is the Material Frontend module to quickly
construct end-user dashboards.

Installation
============

Material Dashboard comes as part of django-material package.

To install it, just add the `material.dashboard` in the
`INSTALLED_APPS` setting

.. code-block:: python

    INSTALLED_APPS = (
         ...
         'material.frontend',
         'material.dashboard',
         ...
    )

After installation, there is the default user dashboard shown. When
any other custom dashboard is registered, they would replace the
default dashboard.


Quick Start
===========

.. code-block:: python

    from material import dashboard
    from django.template.loader import render_to_string

    def users_count(request):
        return render_to_string('material/dashboard/counter.html', {
            'title': 'Users',
            'count': User.objects.count(),
            'icon': '<i class="material-icons">account_circle</i>'
        })

    dashboard.register(
        Dashboard('User', [user_count])
    )

API
===

.. autoclass:: material.dashboard.Dashboard
   :members:

.. autoclass:: material.dashboard.Row
   :members:

.. autoclass:: material.dashboard.Column
   :members:
