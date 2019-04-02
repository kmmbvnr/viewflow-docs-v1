==============
Material Forms
==============

Introduction
============


Django-Material offers the alternative approach to rendering forms in
django. Strong Python/HTML code separation keeps you code DRY and free
from underline HTML/CSS rendering details. Field rendering
customization happens in a template, not in code. Layouts allow
setting relative location and size of fields.

Forms are rendered  with `MaterializeCSS
<http://materializecss.com>`_ framework

.. image:: _static/MaterialForm.png
   :width: 800px
   :target: http://forms.viewflow.io/demo/registration/

Installation
============

django-material tested with Python 2.7/3.6/3.7, django 1.11/2.0/2.1/2.2::

    pip install django-material

Add it into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         'material',
         ...
    )

Quick start
===========

Include formpack javascript and styles into your base template 

.. code-block:: html

    {% include 'material/includes/material_css.html' %}
    {% include 'material/includes/material_js.html' %}


Load the `material_form` template tag library

.. code-block:: html

        {% load material_form %}

And render your form with {% form %} template tag

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% form form=form %}{% endform %}
        <button type="submit" name="_submit" class="btn">Submit</button>
    </form>


Examples
========

Set of samples with live demo and source code are available at http://forms.viewflow.io#forms


License
=======

Django Material is an Open Source project licensed under the terms of the `BSD3 license <https://github.com/viewflow/django-material/blob/master/LICENSE.txt>`_

Django Material Pro has a commercial-friendly license and is distributed as part of Viewflow Pro


Table of  Contents
==================

.. toctree::
   :maxdepth: 2

   forms_templatetags
   forms_layout
   forms_themes
   forms_formsets
   forms_widgets

