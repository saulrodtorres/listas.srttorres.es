from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import *
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
    <form method="POST">
        <label>Descripción:</label>
        <input type="text" name="descripcion" value="%s"><br>
        <label>Estado:</label>
        <input type="text" name="estado" value="%s"><br>
        <input type="submit" value="Actualizar">
    </form>
    </body></html>
    """ % (tarea.descripcion, tarea.estado)
    http_response = HttpResponse(pagina)
    return http_response

def vista_crear_lista(request):
    return HttpResponse('Hola, soy la vista crear lista')

def vista_lista(request):
    #esto debería recibir un ID de lista
    try:
        lista = Lista("nombre aleatorio", "993882")
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, No se ha creado la lista.")
    
    pagina = """<html><body><h1>Lista de tareas de usuario %s:</h1>
        <form method="POST">
        <label>Descripción:</label>
        <input type="text" name="descripcion" value="%s"><br>
        <label>Estado:</label>
        <input type="submit" value="Actualizar">
        </form>
        </body></html>
        """ % (lista.author_id, lista.nombre)
    http_response = HttpResponse(pagina)