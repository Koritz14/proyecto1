from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi segunda aplicacion</h1>" \
    "<a href='youtube/' target='_blank'>ver video</a>")

def video_youtube(request):
    return redirect("https://www.youtube.com/watch?v=5qap5aO4i9A")