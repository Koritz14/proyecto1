from django.urls import path
from . import views # el . significa que se importa desde el mismo directorio

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('youtube/', views.video_youtube, name='video_youtube'),
]