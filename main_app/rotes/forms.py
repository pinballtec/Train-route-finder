from django import forms
from cities.models import City


class RoutesForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    to_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    cities = forms.ModelMultipleChoiceField(
        label='Thought city', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}
        )
    )
    traveling_time = forms.IntegerField(label='time',
    widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'placeholder': 'Travel Time'}))