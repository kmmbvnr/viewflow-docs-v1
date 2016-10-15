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

SpanXX elements are not bound to the material grid classes but used to
determine relative fields width. Each row occupies 12 grid columns.
Elements in Row('elem1', 'elem2') would be rendered in 6 grid columns
each. In the `Row(Span2('elem1'), 'elem2')`, `elem1` would have eight grid
columns and `elem2` four grid columns.


API
===

.. autoclass:: material.Layout
      :members:

.. autoclass:: material.Span
      :members:

.. autoclass:: material.Column
      :members:

.. autoclass:: material.Row
      :members:

.. autoclass:: material.Fieldset
      :members:

.. autoclass:: material.LayoutMixin
    :members:
