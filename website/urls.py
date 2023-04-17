# from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('suggest/',views.suggest, name='suggest')
]
