from django.urls import path
from . import views

urlpatterns = [
    path('', views.cities_showcase, name='first_test'),
]