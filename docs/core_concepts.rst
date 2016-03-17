=============
Core concepts
=============

Flow
====

Flow is the new layer that viewflow adds on top of standard
django Model-View-Template.

Flow class takes all task dependencies logic out of your views. So you
don’t need to change any model status or span background tasks in view
code. This makes views code simple and reusable for different flows.

Flow takes all boilerplate code for specifying permissions and
registering django views in url config.

.. code-block:: python

    class ShipmentFlow(Flow):
        process_cls = ShipmentProcess

        summary_template = """
            Shipment {{ process.shipment.shipmentitem_set.count }} items
            to {{ process.shipment.first_name }} {{ process.shipment.last_name }} / {{ process.shipment.city }}
            """

        start = flow.Start(views.StartView) \
            .Permission('shipment.can_start_request') \
            .Next(this.split_clerk_warehouse)

        ...

.. seealso::

    :class:`viewflow.base.Flow`

Nodes
=====

Each flow contains set of flow nodes. Every element of BPMN diagram
could be transated to corresponding flow node class instance.

Viewflow library contains nodes for user tasks that integrate django
views, background script tasks for various backends like celery, and
common gates for representing process flow logic.

.. seealso::

    :class:`viewflow.flow.start_view.Start`

.. seealso::
    :class:`viewflow.flow.task_view.View`

.. seealso::
    :class:`viewflow.flow.gates.If`

.. seealso::
    :class:`viewflow.flow.gates.Split`

.. seealso::
    :class:`viewflow.flow.gates.Join`

.. seealso::
    :class:`viewflow.flow.end.End`


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

Activation life starts with `initialize` method inside the django
viewflow framework.

Not all task types have all those activation stages. For example for
user view, we can't track when actually user starts execution of the
task.

We can just prepare the activation data on GET request and call `done`
on POST request. We use hidden `activation.management_form` to pass
original start time over this two requests.

On the last part of the livecycle activation is responsible to decide
and activate next tasks activations.

Activation is implemented as separate classes, but if your view is
implementing Activation interface, it would be used instead of the
pre-built activation class. In this case, for the view, `initialize`
method is called before `view.dispatch` method.

.. code-block:: python

    @login_required
    @flow_view()
    def deliver_report(request, activation):
        activation.prepare(request.POST or None)
        form = forms.ReportForm(request.POST or None, instance=activation.process)

        if form.is_valid():
            form.save()
            activation.done()
            return redirect('parcels')

        return render(request, 'parcel/shipmentflow/report.html', {
            'form': form,
            'activation': activation,
        })

.. seealso::

    :doc:`viewflow_activation`


Error handling
==============

Error handling is very important for business application. Broken
state could stop contract signing with an important customer. But
errors in code are happen anyway. That's why viewflow provides two
different strategies for the error processing.

For view tasks any exception in subsequent task activation would
rollback the whole transaction, and view task will be available for
end user again, for the case if they can change input data to pass.

For the jobs, jobs result is committed as soon as the job ends. If error
happens in subsequent task, the subsequent task will be saved in error
state and available for administrator for further processing in django
admin.

Error handling strategy can be customized in activation class.

.. seealso::

    :class:`viewflow.activation.Context`


Flow migrations
===============

You can add a new `task` or change `task.Next` links. Task dependencies are not stored in the
database, and no actions required on new code version deployment.

If you would like to delete a task, you can add a special *Obsolete* node to your flow.
Obsolete node will provide a view to see the historical task state, and ability to admins
to cancel active obsolete tasks. No database content changes is also required.

To rename the task, you can create a django data migration, with simple SQL Update statement

.. code-block:: python

    migrations.RunSQL("""
        UPDATE viewflow_task SET flow_task='helloworld/flows.MyFlow.new_name'
        WHERE flow_task='helloworld/flows.MyFlow.old_name'
    """)

.. seealso::

    :class:`viewflow.flow.obsolete.Obsolete`

