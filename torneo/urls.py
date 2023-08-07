from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('equipos',views.equipos, name='equipos'),
    path('jugadores',views.jugadores, name='jugadores'),
    path('estadisticas',views.estadisticas, name='estadisticas'),
    path('registros',views.registros, name='registros'),
    path('sorteo',views.sorteo, name='sorteo'),
    path('sorteo/<int:id_jugador>',views.get_equipos_include, name='get_equipos_include'),
    path('sorteo/post',views.post_cruce, name='post_cruce'),
    path('sorteo/jugadores',views.get_jugadores, name='get_jugadores'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)