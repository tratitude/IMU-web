from django.contrib import admin
from django.urls import path
from ItemList.views import listone,list

urlpatterns = [
    path('listone/', listone),
    path('list/', list),
    path('admin/', admin.site.urls),
]
