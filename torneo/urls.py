from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('equipos',views.equipos, name='equipos'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)