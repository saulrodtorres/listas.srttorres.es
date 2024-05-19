from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import *


def vista_home(request):
    # Vista para la página principal
    # TODO: leer sobre las colecciones de objetos en django

    return HttpResponse('En la vista home debería aparecer la colección de listas de tareas')

def vista_tarea(request, nombre_autor, nombre_lista, nombre_tarea):
    # Vista para "tarea/<str:nombre_autor>/<str:nombre_lista>/<str:nombre_tarea>/"
    # TODO: tratamiento nombre_autor
    # TODO: tratamiento nombre_lista
    # TODO: tratamiento nombre_tarea

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

def vista_nueva_lista(request):
    # Vista para "lista-tareas/nueva"
    # TODO: El valor del nombre y el author id deben guardarse en el modelo
    # TODO: Debería crearse una plantilla a partir de este formulario

    
    pagina = """<html><body>
        <form method="POST">
        <label>Nombre de la Lista:</label>
        <input type="text" name="descripcion" value="">
        <label>ID de Autor</label>
        <input type="text" name="author_id" value="">
        <input type="submit" value="Guardar">

        </form>

        </body></html>
        """
    http_response = HttpResponse(pagina)
    return http_response

def vista_lista(request, nombre_lista): 
    # Vista para "lista-tareas/<str:nombre_lista>"
    # TODO: debería ser un slug pero de momento en urls es un str
    #esto debería recibir un ID de lista
    try:
        lista = Lista(nombre="nombre aleatorio", author_id="993882")
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, No se ha creado la lista.")
    
    pagina = """<html><body>
        <form method="POST">
        <label>Nombre de la Lista:</label>
        <input type="text" name="descripcion" value="%s"><label>Author ID:%s</label>
        <input type="submit" value="Actualizar">
        </form>

        </body></html>
        """ % (lista.nombre, lista.author_id)
    http_response = HttpResponse(pagina)
    return http_response
