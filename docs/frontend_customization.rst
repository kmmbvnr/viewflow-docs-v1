=============
Customization
=============

Template blocks
===============

You can override `material/frontend/base_site.html` to customize django material admin look and feel.

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

    
`./templates/material/frontend/base_site.html` content::

  {% extends "material/frontend/base.html" %}

  <!-- here you can override any pre-existing in material/frontend/base.html blocks -->

{% block title %}
-----------------

Custom website title::

  {% block title %}The Company Ltd{% endblock %}


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

{% block topbar_links %}
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

