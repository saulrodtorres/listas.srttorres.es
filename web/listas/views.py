from django.shortcuts import render
from django.http import HttpResponse

from .models import Tarea
# Create your views here.
def vista_home(request):
    return HttpResponse('Hola, soy la vista home para home/ y para /')

def vista_tarea(request):
    tarea = Tarea()
    tarea.descripcion = 'Comprar fresas &#x1F353;'
    tarea.estado = 'TODO'
    tarea.author_id = 1003    
    tarea.save()
    pagina = """<html><body>
    <h1>Tarea de usuario:</h1>
    <h3><n>Descripción:</n> %s</h3> 
    <h3><n>Estado:</n> %s</h3>
    <h3><n>Tarea completa:</n> %s</h3>
    </body></html>
    """ % (tarea.descripcion, tarea.estado, tarea.__str__())
    http_response = HttpResponse(pagina)
    return http_response

def vista_listas(request):
    return HttpResponse('Hola, soy la vista listas')