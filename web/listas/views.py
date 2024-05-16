from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import Tarea
# Create your views here.
def vista_home(request):
    return HttpResponse('En la vista home debería aparecer la colección de listas de tareas')

def vista_tarea(request, tarea_id):
    try:
        tarea = Tarea.objects.get(id=tarea_id)
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la tarea con id {tarea_id} no existe. Revisa si el ID es correcto")
    
    pagina = """<html><body>
    <h1>Tarea de usuario:</h1>
    <h3><n>Descripción:</n> %s</h3> 
    <h3><n>Estado:</n> %s</h3>
    <h3><n>Tarea completa:</n> %s</h3>
    </body></html>
    """ % (tarea.descripcion, tarea.estado, tarea.__str__())
    http_response = HttpResponse(pagina)
    return http_response

def vista_lista(request):
    return HttpResponse('Hola, soy la vista listas')