========================
Admin site customization
========================


Application icon
================

``Material Admin`` takes application icons same as ``Material
Frontend`` from `.icon` attribute of application config.


<app>/apps.py::
  
    class PollsAppConfig(AppConfig):
        name = 'polls'
        icon = '<i class="material-icons">flag</i>'




Model icon
==========

Model Icons are taken from `.icon` attribute of model Admin.

<app>/models.py::
  
    @admin.register(models.Poll)
    class PollAdmin(admin.ModelAdmin):
        icon = '<i class="material-icons">bubble_chart</i>'



3d party app icons
==================

3d party application icons could be overriden by custom CSS style.

- Each app icon has the class `admin-appicon-<app_label>`.
- Each model icon has the class - `admin-modelicon-<app_label>-<model_label>`.

You can put custom css directly to the `admin/base_site.html` tempate::

  {% extends "admin/base.html" %}

  {% block extrastyle %}
  <style>
      .admin-appicon-auth:before {
          content: "\e8d3";
      }

      .admin-modelicon-auth-user:before {
          content: "\e7fd";
      }
  </style>
  {% endblock %}

By default icons are rendered with google material design icons font.
The icon codes could be found at https://design.google.com/icons/

You can use other fonts. Just include the correct css in the
`admin/base_site.html` and set the `font-family` in the icon css class::

    {% extends "admin/base.html" %}

    {% block extrastyle %}
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
    <style>
        .admin-appicon-auth:before {
            font-family: FontAwesome;
            content: "\f024";
        }
     </style>
     {% endblock %}


Settings
========

You can provide a custom admin site module in the `MATERIAL_ADMIN_SITE` setting

.. code-block:: python

    MATERIAL_ADMIN_SITE = 'mymodule.admin.admin_site'
