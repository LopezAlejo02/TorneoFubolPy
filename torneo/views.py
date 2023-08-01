from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo
# Create your views here.

def inicio(request):
    return HttpResponse("<h1>Bienvenido</h1>")

def index(request):
    return render(request, 'pages/index.html')
def equipos(request):
    equipos  = Equipo.objects.all()
    return render(request, 'equipos/indice.html', {'equipos': equipos})