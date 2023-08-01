from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def equipos(request):
    equipos  = Equipo.objects.all()
    return render(request, 'equipos/indice.html', {'equipos': equipos})