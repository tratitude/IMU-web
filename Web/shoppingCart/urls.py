from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('index/', views.index, name='index'),
   path('detail/<int:productid>', views.detail, name='detail'),
   path('addtocart/<str:ctype>', views.addtocart, name='addtocart'),
   #path('addtocart/<str:ctype>/<int:productid>', views.addtocart, name='addtocart'),
   url(r'^addtocart/(\w+)/(\d+)/$', views.addtocart),
   url(r'^addtocart/(\w+)/$', views.addtocart),
   path('cart/', views.cart, name='cart'),
   path('cartorder/', views.cartorder, name='cartorder'),
   path('cartok/', views.cartok, name='cartok'),
   path('cartordercheck/', views.cartordercheck, name='cartordercheck'),
]