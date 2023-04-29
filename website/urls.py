from django.urls import path
from . import views


urlpatterns = [
	path('fix/', views.home, name='home'), 
	path('', views.radical, name='radical'), 
	path('suggest/', views.suggest, name='suggest'),
	path('contact/', views.contact, name='contact'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('past', views.past, name='past'),
	path('delete_past/<Past_id>', views.delete_past, name='delete_past'),
]
