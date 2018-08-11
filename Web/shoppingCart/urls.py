from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('index/', views.index, name='index'),
   path(r'^detail/(\d+)/$', views.detail, name='detail'),
   path(r'^addtocart/(\w+)/$', views.addtocart, name='addtocart'),
   path(r'^addtocart/(\w+)/(\d+)/$', views.addtocart),
   path(r'^cart/$', views.cart),
   path(r'^cartorder/$', views.cartorder),
   path(r'^cartok/$', views.cartok),
   path(r'^cartordercheck/$', views.cartordercheck),
]