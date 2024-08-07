from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cotizaciones/', views.cotizaciones_view, name='cotizaciones_view'),
    path('login_operadores/', views.login_operadores, name='login_operadores'),
    path('login_clientes/', views.login_clientes, name='login_clientes'),
    path('pictures_site/', views.pictures_site, name='pictures_site'),
]