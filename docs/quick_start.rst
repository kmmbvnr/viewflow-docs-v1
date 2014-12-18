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

Integration with Karenina
=========================

See :doc:`karenina` installation and configuration instructions.

With karenina you don't need to explicitly specify urls for each flow, just register
the from in the karenina.workflow module, in the flows.py::

    from karenina.workflow import workflow

    class HelloWorldFlow(Flow):
        ...

    workflow.register(HelloWorldFlow)
