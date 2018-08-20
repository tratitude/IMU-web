from django.contrib import admin
from django.urls import path
from ItemList.views import listone,list,upload,show,pd
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('show/',show),
    path('upload/',upload),
    path('listone/', listone),
    path('list/', list),
    path('list/pd/<int:Identity>/', pd),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
