=================
Material Frontend
=================

Introduction
============

Material Frontend is the lightweight alternative to the django admin
allows to build big modular websites.

- Lightweight module extension of django application config
- Ready to use theme build with ``MaterialzeCSS``
- Autocollected site navigation menu
- Fast and smooth navigation with Turbolinks
- CRUD scaffolding build with django class based views
- Out of the box datatables integration.

 
Installation
============

Add `material.frontend` into INSTALLED_APPS settings

.. code-block:: python

    INSTALLED_APPS = (
         'material',
         'material.frontend',
         ...
    )

Add frontend urls into global urlconf module at urls.py

.. code-block:: python

    from material.frontend import urls as frontend_urls

    urlpatterns = [
        ...
        path('', include(frontend_urls)),
    ]


Quick start
===========

If you are creating new django app, you can use `./manage.py
startmodule <app_name>` command.

The command is pretty similar to the `./manage.py startapp`, but it
scaffolds all files required for a `material.frontend` module.

To manually create a new module add `ModuleMixin` to the `AppConfig` definition in the `apps.py` file

.. code-block:: python

    from material.frontend.apps import ModuleMixin

    class MyAppConfig(ModuleMixin, AppConfig):
        name = 'myapp'
        icon = '<i class="material-icons">flight_takeoff</i>'

The application have to have <app_module>/urls.py file, with
a single no-parameterized url with name='index', ex

.. code-block:: python

    urlpatterns = [
            path('', generic.TemplateView.as_view(template_name="sales/index.html"), name="index"),
    ]

All AppConfigs urls will be included into material.frontend.urls automatically under /<app_label>/ prefix
The AppConfig.label, used for the urls namespace.

The menu.html sample

.. code-block:: html

        <ul>
            <li><a href="{% url 'sales:index' %}">Dashboard</a></li>
            <li><a href="{% url 'sales:customers' %}">Customers</a></li>
            {% if perms.sales.can_add_lead %}<li><a href="{% url 'sales:leads' %}">Leads</a></li>{% endif %}
        </ul>

Next, you need to add `myapp.apps.MyAppConfig` to the `INSTALLED_APPS`
setting and run `./manange.py migrate` to get module entry created.

Custom Components
=================

django-material frontend build with Turbolinks and WebCompoments. All shims required to support WebComponents for old webrowsers aready included in the frontend js bundle. The
best way to add a custom javascript to a frontend application is to create a new WebComponent.

There are plenty ways to manage javascript bundles with django. This pages describes how to quick start with webpack tool.

Let's install required dependencies:

.. code-block:: shell

    npm init -y
    npm install --save-dev webpack webpack-cli 
    npm install --save-dev @babel/core @babel/preset-env @babel/register babel-loader

Add to package.json settings for javascript compiler

.. code-block:: javascript

  "babel": {
    "presets": [
      [
        "@babel/preset-env",
        {
          "targets": "> 0.25%, not dead"
        }
      ]
    ]
  }

And create webpack.config.babel.js

.. code-block:: javascript

    import path from 'path';

    const BABEL_LOADER_CONFIG = {
      test: /\.js$/,
      exclude: [path.resolve(__dirname, './node_modules')],
      loader: 'babel-loader',
    };

    const JAVASCRIPT_CONFIG = {
      entry: {
        'my-components': './components/my-components.js',
     },

      output: {
        filename: 'js/[name].min.js',
        path: path.resolve(__dirname, './static/'),
      },

      devtool: 'source-map',

      module: {
        rules: [
        BABEL_LOADER_CONFIG,
        ],
      },
    };

    export default [
      JAVASCRIPT_CONFIG,
    ];

This comfig takes `componnents/my-components.js` file and compiles it to `static/` folder

Let's create our first component in `components/tabs/index.js`

.. code-block:: javascript

    export default class MyTabs extends HTMLElement {
      connectedCallback() {
        this._tabs = M.Tabs.init(this.querySelector('.tabs'));
      }

      disconnectedCallback() {
        this._tabs.destroy();
      }
    }

A browser would call required web component callback with any update to the DOM, regardless of whether it comes from
a full page load, a Turbolinks page change, or an Ajax request. 

Include and register at `components/my-components.js`

.. code-block:: javascript

    import MyTabs from './tabs';

    window.addEventListener('load', () => {
      window.customElements.define('my-tabs', MyTabs);
    });

To add custom js file to all module templates, create a `sales/base_module.html`

.. code-block:: html

    {% extends 'material/frontend/base_module.html' %}
    {% load static %}

    {% block extrahead %}
    <script src="{% static 'js/my-components.min.js' %}"></script>
    {% endblock %}

So now you can run `webpack --mode=production` to get compiled web component. Now you can wrap html tabs definition
in `<my-tabs>...</my-tabs>` tag to get js code initialized.

You can check the full cookbook sample at https://github.com/viewflow/cookbook/tree/master/frontend

------

Examples
========

The live demo of the frontend is available at http://demo.viewflow.io/integration

Demo source code available at the `Github <https://github.com/viewflow/django-material/tree/master/demo/tests/integration>`_
        
License
=======

Material Frontend is distributed as part of `django-material` package under the terms of the `BSD3 license <https://github.com/viewflow/django-material/blob/master/LICENSE.txt>`_

  
Table of Contents
=================

.. toctree::
   :maxdepth: 2

   frontend_modules
   frontend_crud
   frontend_customization
