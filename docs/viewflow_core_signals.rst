=======
Signals
=======

Arguments sent with any of viewflow signals:

   ``sender``
     The flow class.

    ``process``
      Process instance

    ``task``
      Task instance


Flow live cycle signals
=======================

.. autoattribute:: viewflow.signals.flow_started
   :annotation:

Happens when flow start task done

.. autoattribute:: viewflow.signals.flow_finished
   :annotation:

Happens right after process had finished


Task live cycle signals
=======================

.. autoattribute:: viewflow.signals.task_started
   :annotation:

Happens when long running task starts execution


.. autoattribute:: viewflow.signals.task_failed
   :annotation:

    Happens on flow task error

    Additional arguments

    ``exception``
      Exception instance

    ``traceback``
      Traceback object


.. autoattribute:: viewflow.signals.task_finished
   :annotation:

   Happens when any task finished successfully
