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

- No difference between options. If there is enought width, the
  horizontal layout is used. Vertical layout with the box of unselected
  options appearing above the box of selected options used on the small
  screens.

.. attribute:: ModelAdmin.list_editable

- No support for editable lists is implemented

.. attribute:: ModelAdmin.list_max_show_all

- Not implemeted

.. attribute:: ModelAdmin.preserve_filters

- No support for preserve filters is implemented.

.. attribute:: ModelAdmin.save_on_top

- Not implemeted
               
.. attribute:: InlineModelAdmin.min_num

- Option is ignored, inlines always have zero forms

.. attribute:: AdminSite.site_header

- Option is ignored, material admin have no site header.

.. attribute:: AdminSite.index_title

- Option is ignored
