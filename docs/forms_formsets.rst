====================
Formsets and Inlines
====================

**PRO Only**

Formsets and Inlines support is build on the idea from
`django-superform
<https://github.com/gregmuellegger/django-superform>`_ project.
Formset and Inlines are included an procceed as a normal django form
fields.

This keeps your view code free from form-specific details and allows
to use same templating technics from django-material form as for all
rest fields.

Due inactivity, django-superforms code is absorbed into
django-material and now supported as part of django-material Pro
distribution.

Example:
========

To use Formset and Inlines field you have to inherit from `material.forms.Form`::

    from django import forms
    from django.forms import formset_factory
    from material.forms import Form

    class AddressForm(forms.Form):
        line_1 = forms.CharField(max_length=250)
        line_2 = forms.CharField(max_length=250)
        state = forms.CharField(max_length=100)
        city = forms.CharField(max_length=100)
        zipcode = forms.CharField(max_length=10)

        layout = Layout(
            'line_1',
            'line_2',
            'state',
            Row('city', 'zipcode'),
        )

    AddressFormSet = formset_factory(AddressForm, extra=3, can_delete=True)


    class SignupForm(Form):
        username = forms.CharField(max_length=50)
        first_name = forms.CharField(max_length=250)
        last_name = forms.CharField(max_length=250)
        emails = FormSetField(formset_class=EmailFormSet)
        addresses = FormSetField(formset_class=AddressFormSet)

        layout = Layout(
            'username',
            Row('first_name', 'last_name'),
            'emails',
            Stacked(1, 'addresses'),
        )


API
===

.. autoclass:: material.forms.SuperForm
      :members:

.. autoclass:: material.forms.SuperModelForm
      :members:

.. autoclass:: material.forms.FormField
      :members:

.. autoclass:: material.forms.ModelFormField
      :members:

.. autoclass:: material.forms.ForeignKeyFormField
      :members:

.. autoclass:: material.forms.FormSetField
      :members:

.. autoclass:: material.forms.ModelFormSetField
      :members:

.. autoclass:: material.forms.InlineFormSetField
      :members:
