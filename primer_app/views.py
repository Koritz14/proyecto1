from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi aplicacion<h1>")

#mostrar fecha y hora actual
def mostrar_fecha_hora(request):
    ahora = datetime.datetime.now()
    return HttpResponse(f"Fecha y hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")

# acceder a portal URL de inacap
def acceder_inacap(request):
    return HttpResponse("<a href='https://www.inacap.cl/' target='_blank'>Ir a Inacap</a>")