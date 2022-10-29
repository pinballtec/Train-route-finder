from django.urls import path
from . import views
# from .views import Update_City

urlpatterns = [
    path('', views.cities_showcase, name='cities_main'),
    path('<int:pk>/', views.cities_showcase_detail, name='detail_view'),
    path('<int:id>/update', views.update_view, name='update_view'),
    path('<int:id>/delete', views.delete_view, name='delete_view'),
]