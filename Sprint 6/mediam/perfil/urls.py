from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil),
    path('setting/', views.setting),
]