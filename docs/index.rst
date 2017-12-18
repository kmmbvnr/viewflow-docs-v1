=============
Documentation
=============

Introduction
============

Viewflow is the workflow library based on BPMN concepts. BPMN -
Business process modeling and notations - is the widely adopted industry
standard for business process modeling. BPMN provides a standard
notation readily understandable by all business stakeholders. Viewflow
bridges the gap between picture and executable, ready to use web
application.

.. image:: _static/ShipmentProcess.png
   :width: 400px

After more than ten years history of the BPMN standard, it contains
the whole set of battle-proven primitives for all occasions and helps
you to describe all real life business process scenarios. Viewflow
assists you in building a BPMN diagram in code and keep business logic
separate from django forms and views code.

Viewflow suite has a modular design, and you can use viewflow core
library itself, or accompanied with pre-built UI frontend.

Installation
============

django-viewflow works with Python 2.7 and Python 3.4 or greater,
django 1.8/1.9/1.10/1.11::

    pip install django-viewflow

`Viewflow PRO <http://viewflow.io/pro/>`_::

    pip install django-viewflow-pro  --extra-index-url https://pypi.viewflow.io/<licence_id>/simple/

To install from requirements.txt, the following statement could be added on top of the file::

    --extra-index-url https://pypi.viewflow.io/<licence_id>/


3rd party documentation
=======================

You may also interest in the documentation for underline components
of the Viewflow and Django-Material

- `Django - The web framework for perfectionist with deadlines <https://docs.djangoproject.com/>`_
- `Django Filters - reusable application allows users to filter down a queryset <https://django-filter.readthedocs.io/en/latest/>`_
- `Django Rest Framework - the powerful and flexible toolkit for building Web APIs. <http://django-rest-framework.org>`_ 
- `Materialize - The modern responsive front-end framework based on Material Design <http://materializecss.com/>`_
- `Turbolinks - The simple library makes navigating your web application faster <https://github.com/turbolinks/turbolinks>`_
- `Datatables - Advanced interaction controls for any HTML table <https://datatables.net/>`_

Read more about BPMN and Workflow

- `Workflow Patterns <http://www.workflowpatterns.com/>`_
- `Business Process Model and Notation <https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation>`_

Introduction articles

- `state machine != workflow engine <https://jmettraux.wordpress.com/2009/07/03/state-machine-workflow-engine/>`_
- `What Is a BPMN Process (And What Is Not) <http://mainthing.ru/item/715/>`_

Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   viewflow_quickstart
   viewflow_core
   viewflow_flow
   viewflow_rest
   viewflow_frontend
   material_forms
   material_frontend
   thirdparty_packages


License 
======= 

Viewflow is an Open Source project licensed under the
terms of the AGPL - `The GNU Affero General Public License
v3.0 <http://www.gnu.org/licenses/agpl-3.0.html>`_

Viewflow Pro has a commercial-friendly license allowing private forks
and modifications. You can find the commercial license
terms in `COMM-LICENSE
<https://github.com/viewflow/viewflow/blob/master/COMM-LICENSE.txt>`_.
Please see `FAQ <https://github.com/viewflow/viewflow/wiki/Pro-FAQ>`_
for more details.


Copyright
=========

2017 Mikhail Podgurskiy <kmmbvnr@gmail.com>
