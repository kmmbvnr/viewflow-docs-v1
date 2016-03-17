=================
Viewflow Frontend
=================

Material designed frontend module for the Viewflow PRO

.. image:: _static/ViewflowFrontend.png
   :width: 800px


Installation
============

Add `material.frontend` and `viewflow.frontend` into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
        # viewflow
        'viewflow.frontend',
        'viewflow',

        # material
        'material',
        'material.frontend',
        'material.admin',
             ...
    )

*NOTE:* to redefine standard viewfow templates, 'viewflow.frontend' should be added before 'django.contrib.admin'

Add frontend urls into global urlconf module at urls.py

.. code-block:: python

    from material.frontend import urls as frontend_urls

    urlpatterns = [
        ...
        url(r'', include(frontend_urls)),
    ]

In the flows.py file, register a flow in the frontend

.. code-block:: python

    from viewflow import frontent

    class MyFlow(Flow):
        ...

    frontend.register(MyFlow)
