from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Trains
from django.contrib import messages
from .forms import Train_Input
# Create your views here.


def trains_showcase_detail(request, pk):
    cities = get_object_or_404(Trains, id=pk)
    context = {'context': cities}
    return render(request, 'cities/detail_view.html', context)


def trains_showcase(request):
    cities = Trains.objects.all()
    paginator = Paginator(cities, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'cities/index.html', context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(Trains, id=id)

    form = Train_Input(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'Train has  been updated')
        return redirect("first_test")

    context["form"] = form

    return render(request, "trains/update.html", context)


def delete_view(request, id):
    context = {}

    city = get_object_or_404(Trains, id=id)
    if request.method == "POST":
        city.delete()
        return redirect("first_test")

    return render(request, 'cities/delete.html', context)