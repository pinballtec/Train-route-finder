from django.forms import ModelForm
from .models import Trains


class Train_Input(ModelForm):
    class Meta:
        model = Trains
        fields = ['name', 'travel_time', 'arrival_city', 'departure_city']
