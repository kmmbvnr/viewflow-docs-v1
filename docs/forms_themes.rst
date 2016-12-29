======
Themes
======

There are several prebuild thems withing the `django-material`
package. To emable a theme just put the desired theme application into
the `INSTALLED_APPS` setting before the `material` app.

Theme applications contains CSS and images for the material frontend
and admin also.

.. code-block:: python

    INSTALLED_APPS = [
        'material.theme.amber',
        'material',
        ...
    ]
                
List of build-in themes
-----------------------

.. raw:: html

    <span class="theme white-text red darken-4">red</span>
    <span class="theme white-text pink darken-3">pink</span>
    <span class="theme white-text purple darken-3">purple</span>
    <span class="theme white-text deep-purple darken-4">deeppurple</span>
    <span class="theme white-text indigo darken-2">indigo</span>
    <span class="theme white-text blue darken-2">blue</span>
    <span class="theme white-text light-blue darken-4">lightblue</span>
    <span class="theme white-text cyan darken-4">cyan</span>
    <span class="theme white-text teal darken-2">teal</span>
    <span class="theme white-text green darken-4">green</span>
    <span class="theme white-text light-green darken-3">lightgreen</span>
    <span class="theme white-text lime darken-4">lime</span>
    <span class="theme white-text yellow darken-3">yellow</span>
    <span class="theme white-text amber darken-4">amber</span>
    <span class="theme white-text orange darken-4">orange</span>
    <span class="theme white-text deep-orange darken-2">deeporange</span>
    <span class="theme white-text brown darken-2">brown</span>
    <span class="theme white-text blue-grey darken-4">bluegrey</span>

Custom theme generator
----------------------

**PRO Only**

To create a custom theme you can use `./manage.py createtheme` command.

To run it, `yarn` tool need to be installed. See
https://yarnpkg.com/en/docs/install for details.

Example::

    $ python manage.py createtheme --primary-color=1b5e20  --secondary-color=01579b

By default the generated files would be placed in the first directory
from `STATICFILES_DIRS` setting. You can specify custom output
location with `--dest` option.
