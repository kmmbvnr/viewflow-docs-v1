================
What is Viewflow
================

Viewflow is the :abbr:`EDSL (Embedded Domain Specific Language)` based
on :abbr:`BPMN (Business Process Model and Notation)`, and additional
staff required to get working web solution from analytical business
description.

From development point of view, viewflow introduces new layer "Flow"
in addition to common django "Model-View-Template".

Flow Pattern provides a way to explicit definition of user tasks order
and dependencies, extracts business logic out of View layer. 

Viewflow takes care about task state management, concurrent updates,
parallel task synchronization and user permission checking.

Viewflow suite contains from 3 crucial parts.

* **viewflow** - workflow primitives library.
* **viewform** - advanced form rendering library for django.
* **karenina** - prebuild modular workflow interface

You can easily use all of then together, or pick the right part, depends
on level of customization that your want.

.. image:: _static/Karenina.png
   :width: 600px
