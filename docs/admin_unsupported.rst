=========================
Unsupported admin options
=========================

.. attribute:: ModelAdmin.actions_on_top
.. attribute:: ModelAdmin.actions_on_bottom

- Options have no effect

.. attribute:: ModelAdmin.fieldsets

- No support for `wide` and `collapsed` classes

.. attribute:: ModelAdmin.filter_horizontal
.. attribute:: ModelAdmin.filter_vertical

- No difference between options. If there is enough width, the
  horizontal layout used. Vertical layout with the box of unselected
  options appearing above the box of selected options used on the
  small screens.

.. attribute:: ModelAdmin.list_editable

- Not implemented

.. attribute:: ModelAdmin.list_max_show_all

- Not implemented

.. attribute:: ModelAdmin.preserve_filters

- Not implemented

.. attribute:: ModelAdmin.save_on_top

- Not implemented
               
.. attribute:: InlineModelAdmin.min_num

- Option ignored, in lines always have zero forms

.. attribute:: Admin Site.site_header

- Option ignored, material admin have no site header.

.. attribute:: Admin Site.index_title

- Option ignored
