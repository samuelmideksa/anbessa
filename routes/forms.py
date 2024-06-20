from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from routes.models import Route


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'


class RouteSearchForm(forms.Form):
    origin = forms.CharField(max_length=50, required=False, label='Origin')
    destination = forms.CharField(max_length=50, required=False, label='Destination')

    def __init__(self, *args, **kwargs):
        super(RouteSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('search', 'Search', css_class='btn btn-primary'))
