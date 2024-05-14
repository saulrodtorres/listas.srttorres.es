from django.shortcuts import render
from django.http import HttpResponse

from .models import Tarea
# Create your views here.
def vista_home(request):
    return HttpResponse('Hola, soy la vista home para home/ y para /')

def vista_tarea(request):
    tarea = Tarea()
    tarea.descripcion = 'Tarea de prueba'
    tarea.estado = 'TODO'
    tarea.author_id = 1001
    #tarea.save()
    pagina = """<html><body>
    <h1>Tarea de usuario:</h1>
    <h2><n>Descripción:</n> %s</h2> 
    <h3><n>Estado:</n> %s</h3>
    </body></html>
    """ % (tarea.descripcion, tarea.estado)
    http_response = HttpResponse(pagina)
    return http_response

def vista_listas(request):
    return HttpResponse('Hola, soy la vista listas')