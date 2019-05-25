from django.urls import path
from . import views 

app_name = 'users'
 

urlpatterns = [
	path('login/', views.userlogin, name = 'login'),
	path('salir/', views.LogOut, name = 'salir'),
]
 