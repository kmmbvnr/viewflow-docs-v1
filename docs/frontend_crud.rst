====
CRUD
====

`material.frontend` contains several class-based views, allows to
build CRUD interfaces in a few lines of code.

You can start with a simple viewset - a class that collects CRUD view actions for a model in a `myapp/views.py`

.. code-block:: python

    from material.frontend.views import ModelViewSet
    from . import models

    class MyModelViewSet(ModelViewSet):
        model = models.MyModel

And add an entry to the `myapp/urls.py`

.. code-block:: python

    from django.conf.urls import url, include
    from django.views import generic
    from . import views
                
    urlpatterns = [
        url('^$', generic.RedirectView.as_view(url='./mymodel/', permanent=False), name="index"),
        url('^mymodel/', include(views.MyModelViewSet().urls)),
        ...
    ]

`ModelViewSet` class is pretty similar to the
`django.contrib.admin.ModelAdmin` except the all CRUD actions
implemented in the separated class bases views.
    
API
===

.. autoclass:: material.frontend.views.ModelViewSet
      :members:

.. autoclass:: material.frontend.views.CreateModelView
      :members:

.. autoclass:: material.frontend.views.UpdateModelView
      :members:

.. autoclass:: material.frontend.views.DeleteModelView
      :members:

.. autoclass:: material.frontend.views.DetailModelView
      :members:

.. autoclass:: material.frontend.views.ListModelView
      :members:

.. autoclass:: material.frontend.actions.BaseActionView
      :members:

.. autoclass:: material.frontend.actions.DeleteActionView
      :members:

