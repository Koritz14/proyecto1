from django.urls import path
from . import views # el . significa que se importa desde el mismo directorio

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ahora/', views.mostrar_fecha_hora, name='mostrar_fecha_hora'),
    path('inacap/', views.acceder_inacap, name='acceder_inacap'),
]