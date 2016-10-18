==============
Material Admin
==============

Introduction
============

Django Administration interface redesigned to Google Material Design styles

Installation
============

django-material tested with Python 2.7/3.4/3.5, django 1.8/1.9::

    pip install django-material

And add it to INSTALLED_APPS settings

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

Demo
====

The live demo of the admin is available at http://forms.viewflow.io/admin


License
=======

Material Admin is distributed as part of `django-material` package under the terms of the `BSD3 license <https://github.com/viewflow/django-material/blob/master/LICENSE.txt>`_


Table of  Contents
==================

.. toctree::
   :maxdepth: 2

   admin_customization
   admin_unsupported
