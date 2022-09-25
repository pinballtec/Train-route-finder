from django.urls import path
from . import views

urlpatterns = [
    path('', views.cities_showcase, name='first_test'),
    path('<int:id>/', views.cities_showcase_detail, name='detail_view'),
]