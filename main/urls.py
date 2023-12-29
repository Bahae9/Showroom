from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload, name='upload_car'),
    path('search', views.search, name='search'),
    path('remove', views.remove, name='remove'),
    path('api/cars/', views.car_list, name='car_list'),
]
