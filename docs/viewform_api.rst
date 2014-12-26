============
Viewform API
============

Template driven form rendering for django

* Easy redefinition of particular fields rendering
* Strong python/html code separation
* Complex form layouts
* Formsets and js goodies out of the box

Installation
============

django-viewform tested with Python 2.7/3.3, django 1.6/1.7::

    pip install django-viewform

And add it into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         ...
         'viewform',
    )


Quick start
===========

Include formpack javascript and styles into your base template 

.. code-block:: html

        {% include 'viewform/bootstrap3/include_css.html' %}
        {% include 'viewform/bootstrap3/include_js.html' %}

Packs for bootstrap3 and foundation5 are available out of the box

Render your form with {% viewform %} template tag

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% viewform 'viewform/bootstrap3/form.html' form=form %}{% endviewform %}
        <button type="submit" name="_submit" class="btn">Submit</button>
    </form>


Template tags
=============

`viewform` is built around simple concept called viewpart. `Viewpart`
is like django template block, it has a default value and could be
overriden.  But `viewparts` are created dynamically for each form
field, which allows you to redefine specific form field html render output.

Here is the example of rendering form with predefined bootstrap template,
but prepend email field with `@` sign.

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% viewform 'viewform/bootstrap3/form.html' form=form layout=view.layout %}
            {% viewpart form.email.field prepend %}
                 <div class="input-group-addon">@</div>
            {% endviewpart %}
        {% endviewform %}
        <button type="submit" name="_submit" class="btn">Submit</button>
    </form>

There is a lot of other viewparts declared in default templates. See template code for details.
If your widget is so special, just provide `{% viewpart form.my_field.field %}any html code{% endviewpart %}`

Layout
======

Layout object is the way to specify relative fields placements and sizes.

.. code-block:: python

    from viewform import *

    layout = Layout(
        Row('shipment_no', 'description')
        Fieldset("Add to inventory",
                 Row(Span3('product_name'), 'tags'),
                 Row('vendor', 'product_type'),
                 Row(Column('sku',
                            'stock_level',
                            span_columns=4),
                     'gender', 'desired_gender'),
                 Row('cost_price', Span2('wholesale_price'), 'retail_price')))

SpanXX elements are not directly mapped to bootstrap or foundation grid
classes, but used to determine relative fields width. Each row occupies
12 grid columns.  Elements in Row('elem1', 'elem2') would be rendered
in 6 grid coulmns each, and in Row(Span2('elem1'), 'elem2') `elem1`
would be rendered in 8 grid columns, and `elem2` in 4 grid columns.

Layouts rendering itself is specified in template. See
templates/viewform/<tempalte_pack>/layout code folder for details.


ModelForm Views
===============

Viewform library provides  LayoutMixin for model form views, populates
form fields list directly from layout object

.. code-block:: python

    from django import generic
    from viewform import LayoutMixin

    class SampleView(LayoutMixin, generic.ModelFormView):
        layout = Layout(...)



Formset and inlines
===================

With django-extra-views NamedFormsetsMixin you can use inline names
inside viewform layout


.. code-block:: python

    class FormsetView(LayoutMixin,
                      extra_views.NamedFormsetsMixin,
                      extra_views.CreateWithInlinesView):
        model = Shipment

        class ItemInline(extra_views.InlineFormSet):
            model = ShipmentItem
            fields = ['name', 'quantity']

        layout = Layout(
            Row(Column('name', 'city'),
                Column('address_line1', 'address_line2')),
            Inline('Items', ItemInline)
        )

API
===

.. autoclass:: viewform.base.Layout
      :members:

.. autoclass:: viewform.base.Span
      :members:

.. autoclass:: viewform.base.Column
      :members:

.. autoclass:: viewform.base.Row
      :members:

.. autoclass:: viewform.base.Inline
      :members:

.. autoclass:: viewform.base.Fieldset
      :members:

.. autoclass:: viewform.base.LayoutMixin
      :members:
