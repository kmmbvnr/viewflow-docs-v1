================
What is Viewflow
================

Viewflow is the :abbr:`EDSL (Embedded Domain Specific Language)` based
on :abbr:`BPMN (Business Process Model and Notation)`, and addons required to get working web solution from analytical business
description.

From the development point of view, viewflow introduces a new layer "Flow"
in addition to common django "Model-View-Template".

Flow Pattern provides a way of explicit definition of user tasks order
and dependencies, extracts business logic from the View layer. 

Viewflow takes care about task state management, concurrent updates,
parallel task synchronization and user permission checking.

You can easily use all of then together, or pick the right part, depending
on the level of customization you want.

.. image:: _static/Karenina.png
   :width: 600px

.. seealso::
   Announcement on `Reddit <http://www.reddit.com/r/django/comments/2a6qvr/anyone_have_experience_with_finite_state_machines/cit9tyj>`_

.. seealso::
   Historical review on `Hacker News <https://news.ycombinator.com/item?id=8786447>`_
