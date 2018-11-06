from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('login/', views.login),
	path('logout/', views.logout),
	path('index/', views.index),
	path('sign/', views.sign),
	path('modify/',views.modify),
	path('modify_password/',views.modify_password),
]