from django.shortcuts import render, redirect
from ast import literal_eval
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.


def inicio(request):
    return render(request, 'pages/inicio.html')


def jugadores(request):
    jugadores = Jugador.objects.order_by('estrellas')
    return render(request, 'pages/jugadores.html', {'jugadores': jugadores})


def estadisticas(request):
    return render(request, 'pages/estadisticas.html')


def registros(request):
    return render(request, 'pages/registros.html')


def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'pages/equipos.html', {'equipos': equipos})


def sorteo(request):
    jugadores = Jugador.objects.all()
    return render(request, 'pages/sorteo.html', {'jugadores': jugadores})


def get_jugadores(request):
    jugadores = list(Jugador.objects.all().values())
    print(jugadores)
    if (len(jugadores) > 0):
        data = {'message': "Success", 'jugadores': jugadores}

    else:
        data = {'message': "Not Found"}
    return JsonResponse(data)


def get_equipos_include(request, id_jugador):
    consulta = Cruce.objects.filter(jugador_id=id_jugador).values()
    cruces = [cruce['equipo_id'] for cruce in consulta]
    equipos = list(Equipo.objects.filter(id__in=cruces).values())
    if (len(equipos) > 0):
        data = {'message': "Success", 'equipos': equipos}

    else:
        data = {'message': "Not Found"}
    return JsonResponse(data)


def get_equipos_exclude(request, id_jugador):
    consulta = Cruce.objects.filter(jugador_id=id_jugador).values()
    cruces = [cruce['equipo_id'] for cruce in consulta]
    equipos = list(Equipo.objects.exclude(id__in=cruces).values())
    if (len(equipos) > 0):
        data = {'message': "Success", 'equipos': equipos}

    else:
        data = {'message': "Not Found"}
    return JsonResponse(data)


def post_cruce(request):
    if request.method == 'POST':
        data = request.body  # O request.body si estás enviando datos JSON
        # Procesa los datos y realiza las operaciones necesarias en el servidor
        data = literal_eval(data.decode('utf8'))
        id_jugador = data['id_jugador']
        id_equipo = data['id_equipo']
        Cruce(jugador_id = id_jugador, equipo_id = id_equipo).save()
    else:
        pass
    return JsonResponse(data, safe=False)
