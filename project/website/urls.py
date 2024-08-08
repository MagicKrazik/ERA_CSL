from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cotizaciones/', views.cotizaciones_view, name='cotizaciones_view'),
    path('login_operadores/', views.login_operadores, name='login_operadores'),
    path('pictures_site/', views.pictures_site, name='pictures_site'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create_operator/', views.create_operator, name='create_operator'),
    path('operator_list/', views.operator_list, name='operator_list'),
]