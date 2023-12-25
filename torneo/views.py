from django.shortcuts import render, redirect
from ast import literal_eval
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from datetime import datetime
import random
# Functions
def make_fixture(sequence):
    fixture = []
    if len(sequence) < 4:
        
        numeroSorteo = random.randint(1,len(Equipo.objects.all())) 
        sequence['3'] = {'id_jugador':100,'id_equipo': numeroSorteo}
    jugador1 = Jugador.objects.filter(id=sequence['0']['id_jugador']).values()[0]
    equipo1 = Equipo.objects.filter(id=sequence['0']['id_equipo']).values()[0]
    equipo1['escudo'] = '../../' + equipo1['escudo']
    jugador2 = Jugador.objects.filter(id=sequence['1']['id_jugador']).values()[0]
    equipo2 = Equipo.objects.filter(id=sequence['1']['id_equipo']).values()[0]
    equipo2['escudo'] = '../../' + equipo2['escudo']
    jugador3 = Jugador.objects.filter(id=sequence['2']['id_jugador']).values()[0]
    equipo3 = Equipo.objects.filter(id=sequence['2']['id_equipo']).values()[0]
    equipo3['escudo'] = '../../' + equipo3['escudo']
    jugador4 = Jugador.objects.filter(id=sequence['3']['id_jugador']).values()[0]
    equipo4 = Equipo.objects.filter(id=sequence['3']['id_equipo']).values()[0]
    equipo4['escudo'] = '../../' + equipo4['escudo']

    fixture.append({'partido': 1,
                    'jugadorLocal': jugador1, 
                    'equipoLocal': equipo1,
                    'jugadorVisitante': jugador2, 
                    'equipoVisitante': equipo2})
    fixture.append({'partido': 2,
                    'jugadorLocal': jugador3, 
                    'equipoLocal': equipo3,
                    'jugadorVisitante': jugador4, 
                    'equipoVisitante': equipo4})
    fixture.append({'partido': 3,
                    'jugadorLocal': jugador1, 
                    'equipoLocal': equipo1,
                    'jugadorVisitante': jugador4, 
                    'equipoVisitante': equipo4})
    fixture.append({'partido': 4,
                    'jugadorLocal': jugador2, 
                    'equipoLocal': equipo2,
                    'jugadorVisitante': jugador3, 
                    'equipoVisitante': equipo3})
    
    fixture.append({'partido': 5,
                    'jugadorLocal': jugador3, 
                    'equipoLocal': equipo3,
                    'jugadorVisitante': jugador2, 
                    'equipoVisitante': equipo2})
    fixture.append({'partido': 6,
                    'jugadorLocal': jugador4, 
                    'equipoLocal': equipo4,
                    'jugadorVisitante': jugador1, 
                    'equipoVisitante': equipo1})
    fixture.append({'partido': 7,
                    'jugadorLocal': jugador3, 
                    'equipoLocal': equipo3,
                    'jugadorVisitante': jugador4, 
                    'equipoVisitante': equipo4})
    fixture.append({'partido': 8,
                    'jugadorLocal': jugador2, 
                    'equipoLocal': equipo2,
                    'jugadorVisitante': jugador1, 
                    'equipoVisitante': equipo1})
    return fixture
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')


def jugadores(request):
    jugadores = Jugador.objects.order_by('estrellas').exclude(id=100)
    return render(request, 'pages/jugadores.html', {'jugadores': jugadores})


def estadisticas(request):
    return render(request, 'pages/estadisticas.html')


def fixture(request,secuencia):
    try:
        fixture = []
        secuencia = json.loads(secuencia)
        fixtures = make_fixture(secuencia) 
        return render(request, 'pages/fixture.html',{'fixtures':fixtures})
    except:
        return HttpResponse()

def registros(request):
    
    return render(request, 'pages/registros.html')

def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'pages/equipos.html', {'equipos': equipos})


def sorteo(request):
    jugadores = Jugador.objects.all().exclude(id=100)
    return render(request, 'pages/sorteo.html', {'jugadores': jugadores})


def get_jugadores(request):
    jugadores = list(Jugador.objects.all().exclude(id=100).values())
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
