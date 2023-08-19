from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_car_info', views.get_car_info, name='get_car_info'),
]
