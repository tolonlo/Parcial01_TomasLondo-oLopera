from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='home'),
path('vuelos/registrar/', views.create_flight, name='flight_create'),
path('vuelos/', views.flight_list, name='flight_list'),
path('vuelos/estadisticas/', views.flight_stats, name='flight_stats'),
]