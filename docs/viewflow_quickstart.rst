==========
Quick start
==========

This tutorial shows how to create basic Hello World application where
one person starts "Hello, world" request, another one approves it, and
when approved the request sent out.

To follow the tutorial, you need to have Python 3.4+ installed. To run
viewflow with Python 2.7, you need to have PRO license.


Initial steps
=============


Let's create a fresh virtualenv for the demo project. In an empty
directory run the following commands.

.. code-block:: shell

    python3 -m venv env
    source env/bin/activate


At first install viewflow package and django-material to enable pre-build frontend interface.

.. code-block:: shell

    pip install django django-material viewflow


In the current directory, scaffold a new django project:

.. code-block:: shell

   django-admin startproject demo .

Create an app:

.. code-block:: shell

   mkdir demo/helloworld
    ./manage.py startapp hellowold demo/helloworld


Now you should have following file structure:

.. code-block:: shell

    demo/
    ├── admin.py
    ├── apps.py
    ├── helloworld
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    └── wsgi.py


Configuration
=============

Open the `demo/settings.py` and add `viewflow` and `demo.helloworld`
into `INSTALLED_APPS` setting

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'viewflow',
        'demo.helloworld',
    ]


Define models
=============

Open `demo/helloworld/models.py` file and define a process model with `text` and `approved` fields,
to capture process state during execution.

.. code-block:: python

    from django.db import models
    from viewflow.models import Process


    class HelloWorldProcess(Process):
        text = models.CharField(max_length=150)
        approved = models.BooleanField(default=False)


Define flow
===========

Let's take a look at the flow BPMN diagram. We going to map each shape
to the corresponding flow node definition.

.. image:: _static/HelloWorld.png

Open the `demo/helloworld/flows.py` file and define:

.. code-block:: python
           
    from viewflow import flow
    from viewflow.base import this, Flow
    from viewflow.flow.views import CreateProcessView, UpdateProcessView

    from .models import HelloWorldProcess


    class HelloWorldFlow(Flow):
        process_class = HelloWorldProcess

        start = (
            flow.Start(
                CreateProcessView,
                fields=["text"]
            ).Permission(
                auto_create=True
            ).Next(this.approve)
        )

        approve = (
            flow.View(
                UpdateProcessView,
                fields=["approved"]
            ).Permission(
                auto_create=True
            ).Next(this.check_approve)
        )

        check_approve = (
            flow.If(lambda activation: activation.process.approved)
            .Then(this.send)
            .Else(this.end)
        )

        send = (
            flow.Handler(
                this.send_hello_world_request
            ).Next(this.end)
        )

        end = flow.End()

        def send_hello_world_request(self, activation):
            print(activation.process.text)

Viewflow proceeds all applications flows from the `flows.py` file.

- Each flow is a Python class that subclasses `viwflow.base.Flow`
- Each attribute represents a flow task
- To connect flow task altogether, the special `this` object can be
  used to make forward references

`flow.Start` represents a task that performed by a person in a django
view. For the tutorial purpose, we use built-in
`CreateProcessView`. But any class or functional based view annotated
with `@flow.flow_start_view` decorator can be used here.

`flow.Task` is a user task for an existing process.

Tasks execution rights could be restricted by the django permission
system. You can specify a permission name here or set
`auto_create=True` that leads to creating special permission for the
task. In our case, we will have
`helloworld.can_start_helloworldprocess` and
`helloworld.can_approve_helloworldprocess` permissions created. In
addition, two standard permissions would be created
`helloworld.view_helloworldprocess` and
`helloworld.manage_helloworldprocess` for flow list and
administrative actions views.

`flow.If` is the simple exclusive gateway. It selects an outcome
depends on a callable result. For the input, callable gets a task
`activation` - an object that handles current task processing logic,
and that have a `activation.process` and `activation.task` fields
initialized with corresponding model instances.

If the request was approved, the `flow.Handler` would be
executed. `flow.Handler` is the task performed by synchronous call a
python code. Here a `this` reference could be used to point to a flow
instance method, or any Python callable.

`flow.End` finalizes the process and marks it as completed.


Enable frontend
===============

Here we could start to write a lot of templates for flow list, actions,
task details and task execution views. Viewflow comes with prebuild
frontend module, which provides ready to use UI, let's just enable it.

First, adds the required apps to the `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'material',
        'material.frontend',
        'viewflow',
        'viewflow.frontend',
        'demo.helloworld',
    ]

Add frontend URLs into global URL conf module at `demo/urls.py`

.. code-block:: python

    from django.views import generic
    from material.frontend import urls as frontend_urls

    urlpatterns = [
        url(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
        url(r'', include(frontend_urls)),
    ]

At the last step, register our flow in the `viewflow.frontend`.

.. code-block:: python

    from viewflow import frontend

    @frontend.register
    class HelloWorldFlow(Flow):
        ...

Run and explore
===============

Create migrations for the helloworld app.

.. code-block:: shell

    ./manage.py makemigrations helloworld

Apply it

.. code-block:: shell

    ./manage.py migrate

Create an admin user to initial login

.. code-block:: shell

    ./manage.py createsuperuser

Run the server

.. code-block:: shell

    ./manage.py runserver

Go to http://127.0.0.1:8000 and see the viewflow in action!


What's next
===========

.. seealso::

    - :doc:`forms_themes` - frontend colors customization

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   viewflow_cookbook
   viewflow_articles
   viewflow_videos

