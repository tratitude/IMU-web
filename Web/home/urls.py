"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home),
    path('Bulletin/', views.Bulletin),
<<<<<<< HEAD
    path('artical/<int:artical>', views.artical),
    path('artical/update/<int:artical>', views.update_artical),
    path('delete_artical/<int:artical>', views.delete_artical),
=======
    #path('Bulletin/<char:type>/<char:keyword>', views.search_artical),
	path('artical/<int:artical>', views.artical),
	path('delete_artical/<int:artical>', views.delete_artical),
>>>>>>> 10ca378b96dadcbc89af91458e5a2a94c3af6fd3
    path('Bulletin/input_artical/', views.input_artical),
]
