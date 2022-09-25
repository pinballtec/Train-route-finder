from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import City

# Create your views here.


# def test(request):
#     return HttpResponse('first test')

def cities_showcase_detail(request, id):
    cities = get_object_or_404(City, id=id)
    context = {'context': cities}
    return render(request, 'cities/detail_view.html', context)


def cities_showcase(request):
    cities = City.objects.all()
    context = {'context': cities}
    return render(request, 'cities/index.html', context)

