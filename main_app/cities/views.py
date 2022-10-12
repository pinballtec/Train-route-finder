from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import City
from .forms import City_Input


# Create your views here.

# def test(request):
#     return HttpResponse('first test')


def cities_showcase_detail(request, pk):
    cities = get_object_or_404(City, id=pk)
    context = {'context': cities}
    return render(request, 'cities/detail_view.html', context)


def cities_showcase(request):
    if request.method == 'POST':
        form = City_Input(request.POST)
        if form.is_valid():
            form.save()
    form = City_Input()
    cities = City.objects.all()
    paginator = Paginator(cities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/index.html', context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(City, id=id)

    form = City_Input(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'City has  been updated')
        return redirect("first_test")

    context["form"] = form

    return render(request, "cities/update.html", context)


def delete_view(request, id):
    context = {}

    city = get_object_or_404(City, id=id)
    if request.method == "POST":
        city.delete()
        return redirect("first_test")

    return render(request, 'cities/delete.html', context)