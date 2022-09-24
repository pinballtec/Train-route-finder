from django.shortcuts import render
from django.http import HttpResponse
from .models import City

# Create your views here.


# def test(request):
#     return HttpResponse('first test')

def cities_showcase(request):
    cities = City.objects.all()
    context = {'context': cities}
    return render(request, 'cities/index.html', context)