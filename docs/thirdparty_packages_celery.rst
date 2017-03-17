======
Celery
======

**PRO Only**

Cookbook demo project: https://github.com/viewflow/cookbook/tree/master/celery

.. autoclass:: viewflow.contrib.celery.Job
      :show-inheritance:               
      :members:

To use a task with `bind=True` option, wrap `flow_job` in a `method_decorator`::

    from django.utils.decorators import method_decorator

    @shared_task(bind=True)
    @method_decorator(flow_job)
    def send_hello_world_request(self, activation):
        ...


.. autoclass:: viewflow.contrib.celery.JobActivation
      :show-inheritance:               
      :members:

