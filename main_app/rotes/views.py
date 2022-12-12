from django.shortcuts import render, get_object_or_404
from .forms import RoutesForm
from django.contrib import messages
from django.shortcuts import redirect
from trains.models import Trains
from cities.models import City

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


def add_routes(request):
    if request.method == "POST":
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Trains.objects.filter(id__in=trains_lst).select_related(
                'from_city', 'to_city')
            cities = City.objects.filter(
                id__in=[from_city_id, to_city_id]).in_bulk()
            form = RoutesForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'traveling_time': total_time,
                    'trains': qs
                }
            )
            context['form'] = form
        return render(request, 'rotes/create_route.html', context)
    else:
        messages.error(request, "Cant save")
        return redirect('/')


def save_route(request):
    if request.method == "POST":
        form = RoutesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved")
            return redirect('/')
        return render(request, 'rotes/create_route.html', {'form': form})
    else:
        messages.error(request, "Cant save")
        return redirect('/')
