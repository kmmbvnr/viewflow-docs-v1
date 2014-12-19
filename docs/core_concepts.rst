=============
Core concepts
=============

Flow
====

With viewflow library you can describe all your site logic and people
interaction using BPMN-style diagrams. BPMN-style diagrams could be
translated directly to explicit flow definition class where each task
represented as separate class attribute.

Flow class takes all task dependencies logic out of your views. So you
don’t need to change any model status or span background tasks in view
code. This makes views code simple and reusable for different flows.

Also, Flow takes all boilerplate code for specifying permission and
register django views in url config.

.. seealso::

    :class:`viewflow.base.Flow`

Nodes
=====

Each flow contains set of flow nodes. Every element of BPMN diagram
could be transated to corresponding flow node class instance.

Viewflow library contains nodes for user tasks that integrates django
views, background script tasks for various backends like celery, and
common gates for representing process flow ligic.

.. seealso::

    :doc:`viewflow_flow`


Models
======

Viewflow uses simple strategy for storing flow state of your
process. You have a process instance model and associated set of
process tasks. Usually you could be happy with mully-table inheritance
in case if you need to store additional data for the process or even
task. 

Abstract classes are also available, so you can use a flat
strategy for datastore.

.. seealso::

    :doc:`viewflow_models`


Activation
==========

Activation class represents the context of task execution and weaves
declarative flow node definition with process and task instance
livecycle.

Activation live starts with initialize method inside the django
viewflow framework. The orange box shows livecycle part happened on
user level.

Not all task types have all those activation stages. For example for
user view, we can't track when actually user starts execution of the
task.

We can just prepare the activation data on GET request and call done
on POST request. We use hidden activation.management_form to pass
original start time over this two requests.

On the last part of the livecycle activation is responsible to decide
and activate next tasks activations.

Activation is implemented as separate classes, but if your view is
implementing Activation interface, it would be used instead of the
pre-built activation class. In this case, for the view, initialize
method are called before view.dispatch method.

.. seealso::

    :doc:`viewflow_activation`


Error handling
==============

Error handling is very important for business application. Broken
state could stop contract signing with an important customer. But
errors in code are happen anyway. That's why viewflow provides two
different strategies for error processing.

For view tasks any exception in subsequent task activation would
rollback the whole transaction, and view task will be available for
end user again, for the case if they can change input data to pass.

For the jobs, jobs result committed as soon as job ends. If error
happens in subsequent task, subsequent task will be saved in error
state and available for administrator for further processing in django
admin.

Error handling strategy could be customized in activation class.

.. seealso::

    :class:`viewflow.activation.Context`
