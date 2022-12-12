from django import forms
from cities.models import City
from trains.models import Trains
from .models import Rotes


class RoutesForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    to_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), required=False)
    cities = forms.ModelMultipleChoiceField(
        label='Thought city', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}
        )
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Trains.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )
    traveling_time = forms.IntegerField(label='time',
    widget=forms.NumberInput(
        attrs={'class': 'form-control',
               'placeholder': 'Travel Time'}))

    class Meta:
        model = Rotes
        fields = '__all__'