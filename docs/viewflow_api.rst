============
Viewflow API
============

.. toctree::
   :maxdepth: 2

   viewflow_activation


Context
=======

.. autoclass:: viewflow.activation.Context


Flow
====

.. autoclass:: viewflow.flow.base.Node

Start View
----------

.. autofunction:: viewflow.flow.start_view.flow_start_view

.. autoclass:: viewflow.flow.start_view.ManagedStartViewActivation

.. autoclass:: viewflow.flow.start_view.BaseStart

.. autoclass:: viewflow.flow.start_view.Start

Task View
---------

.. autofunction:: viewflow.flow.task_view.flow_view

.. autoclass:: viewflow.flow.task_view.ManagedViewActivation

.. autoclass:: viewflow.flow.task_view.BaseView

.. autoclass:: viewflow.flow.task_view.View

Function tasks
--------------

.. autoclass:: viewflow.flow.func.StartFunction

.. autoclass:: viewflow.flow.func.FuncActivation

.. autoclass:: viewflow.flow.func.FlowFunc

.. autofunction:: viewflow.flow.func.flow_func

.. autoclass:: viewflow.flow.func.Function

.. autoclass:: viewflow.flow.func.HandlerActivation

.. autoclass:: viewflow.flow.func.Handler

Signals tasks
-------------

.. autoclass:: viewflow.flow.signal.StartSignal

.. autoclass:: viewflow.flow.signal.Receiver

.. autofunction:: viewflow.flow.signal.flow_signal

.. autoclass:: viewflow.flow.signal.Signal

Gates
-----

.. autoclass:: viewflow.flow.gates.IfActivation

.. autoclass:: viewflow.flow.gates.If

.. autoclass:: viewflow.flow.gates.SwitchActivation

.. autoclass:: viewflow.flow.gates.Switch

.. autoclass:: viewflow.flow.gates.JoinActivation

.. autoclass:: viewflow.flow.gates.Join

.. autoclass:: viewflow.flow.gates.SplitActivation

.. autoclass:: viewflow.flow.gates.Split

End
---

.. autoclass:: viewflow.flow.end.End



Exceptions
==========

.. autoclass:: viewflow.exceptions.FlowRuntimeError

.. autoclass:: viewflow.exceptions.FlowLockFailed


Lock
====

Models
======

Admin Integration
=================


Templates
=========


Template tags
=============

Test
====

Views
=====
