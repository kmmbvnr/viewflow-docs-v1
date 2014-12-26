========
Karenina
========

Quickstart goodies for happy business apps and internal tools development with django.

.. image:: _static/Karenina.png
   :width: 600px


Quick Start
===========

Install karenina and viewform library::

    pip install viewform karenina --extra-index-url https://pypi.viewflow.io/<licence_id>/simple/

Put following applications on top of `INSTALLED_APPS` option::

    INSTALLED_APPS = (
        'karenina.theme',
        'karenina.modules',
        'karenina.management',
        'karenina.workflow',
        'bootstrap_admin',
        'compressor',
        'easy_pjax',
        'viewform',
        ...
    )

Configure required context processors::

    from django.conf import global_settings
    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'karenina.modules.context_processors.modules',
    )

Configure static file finders::

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    )
    
And add following additional settings::

    LOGIN_URL = '/management/login/'
    LOGIN_REDIRECT_URL = '/'
    BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


API
===

karenina.modules
----------------

.. autoclass:: karenina.modules.apps.BaseModulesConfig
      :members:

.. autoclass:: karenina.modules.apps.ModulesDiscoverConfig
      :members:

.. autoclass:: karenina.modules.base.Module
      :members:

.. autoclass:: karenina.modules.base.InstallableModule
      :members:

.. autofunction:: karenina.modules.context_processors.modules

.. autoclass:: karenina.modules.models.Module
      :members:

.. autoclass:: karenina.modules.models.ModuleManager
      :members:

.. autoclass:: karenina.modules.registry.Registry
      :members:

.. autoclass:: karenina.modules.urlconf.ModuleURLResolver
      :members:


karenina.management
-------------------

.. autoclass:: karenina.management.modules.Admin
      :members:

.. autoclass:: karenina.management.views.modules_list
      :members:

karenina.workflow
-----------------

.. autoclass:: karenina.workflow.modules.Workflow
      :members:

.. autoclass:: karenina.workflow.flowsite.FlowSite
      :members:
