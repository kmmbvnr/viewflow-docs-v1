========================
Admin site customization
========================


Application icon
================

``Material Admin`` takes application icons same as ``Material
Frontend`` from an `.icon` attribute of application config.


<app>/apps.py::
  
    class PollsAppConfig(AppConfig):
        name = 'polls'
        icon = '<i class="material-icons">flag</i>'




Model icon
==========

Model Icons are taken from an `.icon` attribute of model Admin.

<app>/models.py::
  
    @admin.register(models.Poll)
    class PollAdmin(admin.ModelAdmin):
        icon = '<i class="material-icons">bubble_chart</i>'



3d party app icons
==================

3d party application icons could be overridden by custom CSS style.

- Each app icon has the class `admin-appicon-<app_label>`.
- Each model icon has the class - `admin-modelicon-<app_label>-<model_label>`.

You can put custom css directly to the `admin/base_site.html` template::

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


Template blocks
===============

You can override `admin/base_site.html` to customize django material admin look and feel.

To override any application template in django, you can set `DIRS`
settings for the django template loader::

    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # ./templates/ subdirectory is located at the same folder as ./manage.py
            os.path.join(BASE_DIR, 'templates')
        ],
         ...
     }

    
`./templates/admin/base_site.html` content::

  {% extends "admin/base.html" %}

  <!-- here you can override any pre-existing in admin/base.html blocks -->

{% block extracss %}
--------------------

Include any additionaly css files::

  {% block extracss %}
      <link href="{% static 'myapp/css/mystyle.css' %}"  rel="stylesheet">
  {% endblock %}

{% block js %}
--------------

Include additional js files::

  {% block js %}
      {{ block.super }}
      <script src="{% static 'myapp/js/myapp.js' %}"></script>
  {% endblock %}

{% block userphoto %}
---------------------

User avatar on the sidebar::

   {% load avatar_tags %}
   {% block userphoto %}
   <a href="#">{% avatar user 65 class="circle" %}</a>
   {% endblock %}

{% block sidenav_items %}
-------------------------

Include additional items on the side bar::

   {% block sidenav_items %}
       {{ block.super }}
       <li><a class="collapsible-header" href="http://viewflow.io">Viewflow</a></li>
   {% endblock %}

{% block userlinks %}
---------------------

Additional links on the top bar::

    {% block userlinks %}
    <li>
      <a class="dropdown-button" href="#!" data-activates="user-menu">
           <i class="material-icons right">arrow_drop_down</i>Menu
      </a>
    </li>
    <ul id="user-menu" class="dropdown-content"  style="min-width:200px">
        <li><a href="#">Item 1</li>
        <li><a href="#">Item 2</li>
    </ul>
    {{ block.super }}
    {% endblock %}


See also
========

Django documenation - `Overriding admin templates
<https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates>`_


Settings
========

You can provide a custom admin site module in the `MATERIAL_ADMIN_SITE` setting

.. code-block:: python

    MATERIAL_ADMIN_SITE = 'mymodule.admin.admin_site'
