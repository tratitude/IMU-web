from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	#path('login/', auth_views.LoginView.as_view(template_name='/account/login.html')),
    path('login/', views.login),
	path('logout/', views.logout),
	path('index/', views.index),
	path('sign/', views.sign),
	path('modify/',views.modify),
	path('modify_password/',views.modify_password),
	path('list_order/', views.list_order)
]