=============
Template Tags
=============

{% form %}
==========

Renders material desing styled form.

Options:


* `form` - form instance to render, if not specified, takes from from `form` context variable
* `layout` - form layout object, by default first from `layout` then `view.layout` context variable
* `template` - template to render a form, default 'material/form.html'


Example:

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% form form=customer_form layout=form.layout %}{% endform %}
   </form>


{% part %}
==========

`django-material` forms processing is built around simple concept
called *part*. `part` is like django template block, it has a default
value and could be overriden.  But `parts` are created dynamically for
each form field, which allows you to redefine specific form field html
render output.

Here is the example of rendering form with but prefix email field with email icon.

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% form %}
            {% part form.email prefix %}<div class="input-group-addon">@</div>{% endpart %}
        {% endform %}
        <button type="submit" name="_submit" class="btn">Submit</button>
    </form>

There is a lot of other parts declared in default templates. See
template code for details.  If your widget is so special, you can
completly override its rendering 

.. code-block:: html

    {% part form.my_field %}any html code here{% endpart %}

List of common parts
--------------------

Each field template could have own parts available for redefinition.

Here is the list of common parts, available in most of field templates::

    {% part field prefix %}{% endpart %}
    {% part field control %}{% endpart %}
    {% part field label %}{% endpart %}
    {% part field help_text %}{% endpart %}
    {% part field errors %}{% endpart %}

Widget specific parts
---------------------

CheckboxSelectMultiple
~~~~~~~~~~~~~~~~~~~~~~

Number of columns to render checkboxes::
  
    {% part field columns %}1{% endpart %}
    
{% attr %}
==========

The tag allows to add or override specific attribute in the rendered
html.

Here are few examples.

Set field div-wrapper class attribute::
  
    {% attr form.field 'group' class %}col s12 m6 l4{% endattr %}

Add `data-validate` attribute the the `<label>` tag::
  
    {% attr form.field 'label' data-validate%}1{% endattr %}

Append `blue` to the list of classes of the `<input>` tag::
  
    {% attr form.field 'widget' 'class'  append %}blue{% endattr %}


Widget specific attributes
--------------------------

RadioSelect
~~~~~~~~~~~

Render radio sleectin one line::
  
    {% attr form.field 'group' class append %}inline{% endattr %}
