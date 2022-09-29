from django.forms import ModelForm
from .models import City


class City_Input(ModelForm):
    class Meta:
        model = City
        fields = ['name', ]
