from django.contrib import admin
from django.urls import path
from ItemList.views import list,pd,listfor
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('list/', list),
    path('list/<str:ord>', listfor),
    path('list/pd/<int:Identity>/', pd),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
