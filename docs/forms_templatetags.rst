=============
Template Tags
=============

{% form %}
==========

Renders the form.

Options:

* `form` - form instance to render, if not specified, takes from from `form` context variable
* `layout` - the layout object, by default takes first from `layout` then `view.layout` context variable
* `template` - template to render a form, default 'material/form.html'


Example:

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% form form=customer_form layout=form.layout %}{% endform %}
   </form>


{% part %}
==========

In the `django-material` forms processing build around simple the concept
called `part`. `part` is like django template block, it has a default
value and could be overridden.  But `parts` are created dynamically
for each form field, which allows you to redefine particular form
field HTML code.

Here is the example of rendering form with but prefix email field with email icon.

.. code-block:: html

    <form method="POST">
        {% csrf_token %}
        {% form %}
            {% part form.email prefix %}<div class="input-group-addon">@</div>{% endpart %}
        {% endform %}
        <button type="submit" name="_submit" class="btn">Submit</button>
    </form>

There are a lot of other parts declared in default templates. See
template code for details. Even whole field rendering could be overridden.

.. code-block:: html

    {% part form.my_field %}any html code here{% endpart %}

List of standard parts
----------------------

Each field template could have own parts available for redefinition.

Here is the list of standard parts, available in most of the fields templates::

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
HTML.

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

Render radio options in one line::
  
    {% attr form.field 'group' class append %}inline{% endattr %}
