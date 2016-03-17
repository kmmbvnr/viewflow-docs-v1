===========
Quick Start
===========


Installation
============

Viewflow requires Python 3.3 or greater, django 1.6::

    pip install django-viewflow

For installing `Viewflow-Pro <http://viewflow.io/#viewflow_pro>`_ with Python 2.7 support and additional features::

    pip install django-viewflow-pro  --extra-index-url https://pypi.viewflow.io/<licence_id>/simple/

Or inside of your project by adding the following statement to requirements.txt::

    --extra-index-url https://pypi.viewflow.io/<licence_id>/

And add it into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         ...
         'viewflow',
    )


Hello, world flow
=================

Let's define basic Hello Process where one could start hello world request, another person approves it,
and as soon as the request is approved it should be send into background.

Start with process database model definition

.. code-block:: python

    from django.db import models
    from viewflow.models import Process

    class HelloWorldProcess(Process):
        text = models.CharField(max_length=150)
        approved = models.BooleanField(default=False)

Define the actual task that says Hello to the World in `tasks.py`

.. code-block:: python

    import os

    from celery import shared_task
    from viewflow.flow import flow_job

    @shared_task()
    @flow_job()
    def send_hello_world_request(activation):
        with open(os.devnull, "w") as world:
            world.write(activation.process.text)


To make the above code work just put the following flow definition in `flows.py` module from your django application.

.. code-block:: python

    from viewflow import flow, lock
    from viewflow.base import this, Flow
    from viewflow.contrib import celery
    from viewflow.views import StartView, ProcessView

    from . import models, tasks


    class HelloWorldFlow(Flow):
        process_cls = models.HelloWorldProcess
        lock_impl = lock.select_for_update_lock

        start = flow.Start(StartView, fields=["text"]) \
            .Permission(auto_create=True) \
            .Next(this.approve)

        approve = flow.View(ProcessView, fields=["approved"]) \
            .Permission(auto_create=True) \
            .Next(this.check_approve)

        check_approve = flow.If(cond=lambda p: p.approved) \
            .OnTrue(this.send) \
            .OnFalse(this.end)

        send = celery.Job(tasks.send_hello_world_request) \
            .Next(this.end)

        end = flow.End()

`Flow` class contains all urls required for the task processing.

.. code-block:: python

    from django.conf.urls import patterns, url, include
    from viewflow import views as viewflow
    from .helloworld.flows import HelloWorldFlow

    urlpatterns = patterns('',
        url(r'^helloworld/', include([
            HelloWorldFlow.instance.urls,
            url('^$', viewflow.ProcessListView.as_view(), name='index'),
            url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
            url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
            url('^details/(?P<process_pk>\d+)/$', viewflow.ProcessDetailView.as_view(), name='details'),
        ], namespace=HelloWorldFlow.instance.namespace), {'flow_cls': HelloWorldFlow}))


Your Hello World process is ready to go. If you run the development server
locally, go to http://localhost:8000/helloworld/ and step through the workflow.

.. seealso::

    :doc:`viewflow_frontend`
