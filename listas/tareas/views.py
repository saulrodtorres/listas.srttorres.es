from django.http import HttpResponse
from django.shortcuts import render
from .models import Tarea # Importa la clase Tarea del archivo models.py


# Create your views here.

def vista_tarea(request):
    tarea = Tarea()
    tarea.descripcion = 'Tarea de prueba'
    tarea.estado = 'TODO'
    tarea.author_id = 1001
    tarea.save()
    pagina = "<html><body><h1>La tarea:</h1> <h2>%s</h2></body></html>" % tarea
    http_response = HttpResponse(pagina)
    return http_response