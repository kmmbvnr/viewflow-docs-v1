=======
Widgets
=======

**PRO Only**

`AjaxModelSelect` and `AjaxMultipleModelSelect` provides autocomplete widgets for the django-material.
Unlike other implementations, they not requires a separate autocomplete view registered. Instead, the
autocomplete widgets sends HTTP OPTIONS request to the same view. So the same user permissions check
would be applied, and the same form could be utilized to form autocomplete suggestions list.

Function based view integration sample::

  from django.http import JsonResponse, QueryDict
  from material.forms import AjaxModelSelect, get_ajax_suggestions

  class AddressForm(forms.ModelForm):
      class Meta:
          model = Address
          fields = ['city', 'street', 'flat']
          widgets = {
              'city': AjaxModelSelect(lookups=['name__icontains'])
          }

   def address(request):
       form = AddressForm(request.POST or None)
       
       if request.method == 'OPTIONS':
           query = self.request.META.get('HTTP_X_REQUEST_AUTOCOMPLETE', self.request.body)
           options = QueryDict(query, encoding=request.encoding)
           field = form.base_fields.get(options.get('field'))
           query = options.get('query')
                 
           if field is None or query is None:
               return JsonResponse({'error': 'Field or Query is missing'}, status=400)
           return JsonResponse({
               'suggestions': get_ajax_suggestions(field, query)
           })
       elif form.is_valid():
           form.save()
           return redirect('success')

       return render(request, 'address.html', {'form': form})

       
Class based view integration sample::

  from material.forms import FormAjaxCompleteMixin

  class AddressFormView(FormAjaxCompleteMixin, generic.CreateView):
      model = Address
      form_class = AddressForm


.. seealso::

   `Redesigning an autocomplete for Django <https://medium.com/@viewflow/redesigning-an-autocomplete-for-django-1994fd07c0a6>`_

API
===

.. autoclass:: material.forms.AjaxModelSelect

.. autoclass:: material.forms.AjaxMultipleModelSelect

.. autoclass:: material.forms.FormAjaxCompleteMixin

.. autofunction:: material.forms.get_ajax_suggestions
