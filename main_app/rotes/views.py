from django.shortcuts import render, get_object_or_404
from .forms import RoutesForm
from django.contrib import messages

from .utils import get_routes


# Create your views here.


def home(request):
    if request.method == 'POST':
        form = RoutesForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as error:
                messages.error(request, error)
                return render(request, 'rotes/home.html', {'form': form})
            return render(request, 'rotes/home.html', context)
        return render(request, 'rotes/home.html', {'form': form})
    else:
        form = RoutesForm(request.POST)
        messages.error(request, 'No data')
        return render(request, 'rotes/home.html', {'form': form})


def find_routes(requests):
    pass
