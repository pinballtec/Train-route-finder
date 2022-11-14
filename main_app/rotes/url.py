from django.urls import path
from . import views
# from .views import Update_City

urlpatterns = [
    path('', views.home, name='routes_home'),
]