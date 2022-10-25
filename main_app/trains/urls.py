from django.urls import path
from . import views

urlpatterns = [
    path('', views.trains_showcase, name='first_test'),
path('<int:pk>/', views.trains_showcase_detail, name='detail_view'),
    path('<int:id>/update', views.update_view, name='update_view'),
    path('<int:id>/delete', views.delete_view, name='delete_view'),
]