=============
Viewflow Flow
=============

.. autoclass:: viewflow.base.Flow
      :members:

Base Node
=========

.. autoclass:: viewflow.flow.base.Node
      :members:

Start View
==========
.. image:: _static/StartView.png

.. autofunction:: viewflow.flow.start_view.flow_start_view

.. autoclass:: viewflow.flow.start_view.ManagedStartViewActivation
      :members:

.. autoclass:: viewflow.flow.start_view.BaseStart
      :members:

.. autoclass:: viewflow.flow.start_view.Start
      :members:

Task View
=========
.. image:: _static/TaskView.png

.. autofunction:: viewflow.flow.task_view.flow_view

.. autoclass:: viewflow.flow.task_view.ManagedViewActivation
      :members:

.. autoclass:: viewflow.flow.task_view.BaseView
      :members:

.. autoclass:: viewflow.flow.task_view.View
      :members:

Function tasks
==============

.. autoclass:: viewflow.flow.func.StartFunction
      :members:

.. autoclass:: viewflow.flow.func.FuncActivation
      :members:

.. autoclass:: viewflow.flow.func.FlowFunc
      :members:

.. autofunction:: viewflow.flow.func.flow_func

.. autoclass:: viewflow.flow.func.Function
      :members:

.. autoclass:: viewflow.flow.func.HandlerActivation
      :members:

.. autoclass:: viewflow.flow.func.Handler
      :members:

Signals tasks
=============

.. autoclass:: viewflow.flow.signal.StartSignal
      :members:

.. autoclass:: viewflow.flow.signal.Receiver
      :members:

.. autofunction:: viewflow.flow.signal.flow_signal

.. autoclass:: viewflow.flow.signal.Signal
      :members:

Subprocesses
============

.. autoclass:: viewflow.flow.subprocess.Subprocess
      :members:

.. autoclass:: viewflow.flow.subprocess.NSubprocess
      :members:

Gates
=====
.. image:: _static/GateTask.png

.. autoclass:: viewflow.flow.gates.IfActivation
      :members:

.. autoclass:: viewflow.flow.gates.If
      :members:

.. autoclass:: viewflow.flow.gates.SwitchActivation
      :members:

.. autoclass:: viewflow.flow.gates.Switch
      :members:

.. autoclass:: viewflow.flow.gates.JoinActivation
      :members:

.. autoclass:: viewflow.flow.gates.Join
      :members:

.. autoclass:: viewflow.flow.gates.SplitActivation
      :members:

.. autoclass:: viewflow.flow.gates.Split
      :members:

Obsolete
========

.. autoclass:: viewflow.flow.obsolete.Obsolete

End
===

.. image:: _static/EndTask.png

.. autoclass:: viewflow.flow.end.End
      :members:


Table of Contents
=================

.. toctree::
   :maxdepth: 2
   :titlesonly:

   viewflow_flow_activation
   viewflow_flow_nodes
   viewflow_flow_views_actions
   viewflow_flow_views_detail
   viewflow_flow_views_list
   viewflow_flow_views_start
   viewflow_flow_views_task
   viewflow_flow_viewset
   viewflow_flow_tempatetags
   viewflow_flow_views_mixins
   viewflow_flow_views_utils
