from django import forms
from cities.models import City


class RoutesForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    to_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    traveling_time = forms.IntegerField(label='time',
    widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'placeholder': 'Travel Time'}))

