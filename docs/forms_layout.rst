============
Forms Layout
============

Layout
======

Layout object is the way to specify relative fields placements and sizes.

.. code-block:: python

    from material import *

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

SpanXX elements are not to material grid classes, but used to
determine relative fields width. Each row occupies 12 grid columns.
Elements in Row('elem1', 'elem2') would be rendered in 6 grid coulmns
each, and in Row(Span2('elem1'), 'elem2') `elem1` would be rendered in
8 grid columns, and `elem2` in 4 grid columns.

Layouts rendering itself is specified in template.


API
===

.. autoclass:: material.base.Layout
      :members:

.. autoclass:: material.base.Span
      :members:

.. autoclass:: material.base.Column
      :members:

.. autoclass:: material.base.Row
      :members:

.. autoclass:: material.base.Fieldset
      :members:
