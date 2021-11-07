=============
Viewflow REST
=============

**PRO Only**

`viewflow.rest` package provides a flow implementation with the REST interface.

- /flows/ - List of available flows
- /processes/ - List of processes
- /tasks/ - List of tasks from all flows

Per flow API:

- /flows/<flow_label>/ - Flow description
- /flows/<flow_label>/chart/ - SVG flow visualization
- /processes/<flow_label>/ - List of flow instances
- /tasks/<flow_label>/ - List of flow tasks

Each flow node could have own API set,

See also the http://demo.viewflow.io/workflow/api/ for the Swagger documentation of each endpoint.

Quick start
===========

`viewflow.rest` depends on `djangorestframework>=3.6` and `django-rest-swagger>=2.1`


Start with adding `viewflow`, `viewflow.rest` and dependencies to the `INSTALLED_APPS` settings

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        'viewflow',
        'viewflow.rest',
        'rest_framework',
        'rest_framework_swagger',
    ]

Flows could be defined in the `<app>/flows.py`. Here is the same
HelloFlow as in the :doc:`viewflow_quickstart` but with REST
interface.


.. code-block:: python

    from viewflow import rest
    from viewflow.base import this, Flow
    from viewflow.rest import flow, views

    from . import models


    class HelloRestFlow(Flow):
        process_class = models.HelloRestProcess

        start = flow.Start(
            views.CreateProcessView, fields=['text']
        ).Permission(
            auto_create=True
        ).Next(this.approve)

        approve = flow.View(
            views.UpdateProcessView, fields=['approved'],
            task_description="Message approvement required",
            task_result_summary="Message was {{ process.approved|yesno:'Approved,Rejected' }}"
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)

        check_approve = flow.If(
            cond=lambda act: act.process.approved
        ).Then(
            this.send
        ).Else(
            this.end
        )

        send = flow.Handler(
            this.send_message
        ).Next(this.end)

        end = flow.End()

        def send_message(self, activation):
           print(activation.process.text)               

In case if you use `viewflow.frontend` you can register flow in it,
and get nice rendered SWAGGER api spec.

.. code-block:: python
    
    from viewflow import rest

    @rest.register
    class HelloWorldFlow(Flow):
        ...

Don't forged to enable the frontend, see :doc:`viewflow_quickstart` for details.

Without frontend you need directly include flowset urls in the django's URL config.

.. code-block:: python

    from django.urls import path, include
    from viewflow.rest.viewset import FlowViewSet
    from .flows import HelloWorldFlow

    hello_urls = FlowViewSet(HelloWorldFlow).urls

    urlpatterns = [
        path('workflow/api/helloworld/', include(hello_urls, namespace='helloworld'))
    ]


                
Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   viewflow_rest_activation
   viewflow_rest_nodes
   viewflow_rest_serializers
   viewflow_rest_views
   viewflow_rest_viewset
