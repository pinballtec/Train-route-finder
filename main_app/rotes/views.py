from django.shortcuts import render
from .forms import RoutesForm

# Create your views here.


def home(request):
    form = RoutesForm()
    return render(request, 'rotes/home.html', {'form': form})