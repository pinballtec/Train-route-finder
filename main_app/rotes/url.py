from django.urls import path
from . import views
# from .views import Update_City

urlpatterns = [
    path('home_routes/', views.home, name='routes_home'),
    path('add_route/', views.add_routes, name='add_route'),
    path('save_route/', views.save_route, name='save_route'),
]