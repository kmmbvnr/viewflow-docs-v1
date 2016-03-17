==============
Material Admin
==============

Django Administration interface redisigned to Google Material Design styles

**Admin development is on initial stage. Only basic admin features are available.**

http://forms.viewflow.io/admin

.. image:: _static/MaterialAdmin.png
   :width: 800px

Installation
============

django-material tested with Python 2.7/3.4/3.5, django 1.8/1.9::

    pip install django-material

And add it into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         'material',
         'material.admin',
         ...
    )

*NOTE:* 'material.admin' must be added before 'django.contrib.admin'

Ensure that `django.template.context_processors.request` in your template context processor settings list

.. code-block:: python

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]


Settings
========

You can provide a custom admin site module in the `MATERIAL_ADMIN_SITE` setting

.. code-block:: python

    MATERIAL_ADMIN_SITE = 'mymodule.admin.admin_site'
