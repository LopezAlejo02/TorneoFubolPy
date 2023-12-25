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
    path('fixture/secuencia/<str:secuencia>',views.fixture, name='fixture'),
    path('sorteo',views.sorteo, name='sorteo'),
    path('sorteo/<int:id_jugador>',views.get_equipos_include, name='get_equipos_include'),
    path('sorteo/post',views.post_cruce, name='post_cruce'),
    path('sorteo/jugadores',views.get_jugadores, name='get_jugadores'),
    path('sorteo/exclude/<int:id_jugador>',views.get_equipos_exclude, name='get_equipos_exclude'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)