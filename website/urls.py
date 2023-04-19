# from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('suggest/', views.suggest, name='suggest'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
