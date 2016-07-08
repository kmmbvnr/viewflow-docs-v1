===========
Quick Start
===========

           
Installation
============

django-material tested with Python 2.7/3.4/3.5, django 1.8/1.9::

    pip install django-material

And add it into INSTALLED_APPS settings

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
