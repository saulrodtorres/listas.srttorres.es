from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader # Para cargar plantillas


from .models import *


def vista_home(request):
    # Vista para la página principal
    # TODO: leer sobre las colecciones de objetos en django

    return HttpResponse('En la vista home debería aparecer la colección de listas de tareas')

def vista_tarea(request, slug_nombre_autor, lista_pk, tarea_pk):
    # Vista para "<str:slug_nombre_autor>/lista-tareas/<int:slug_nombre_lista>/tarea/<str:slug_nombre_tarea>"
    print(f"slug_nombre_autor: {slug_nombre_autor}, lista_pk: {lista_pk}, tarea_pk: {tarea_pk}")

    try:
        tarea_actual = Tarea.get_tarea_por_pk(pk=tarea_pk)
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {tarea_pk} no existe. Revisa si el PK de la tarea es correcta")
    
    tarea = Tarea.objects.get(pk=tarea_pk)#esto está mal, debería ser por lista_id
    template = loader.get_template("listas/tarea.html")
    context = {                
        "tarea": tarea_actual,                          #Esto es un objeto Tarea
    }
    print(tarea_actual)
    return HttpResponse(template.render(context, request))

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

def vista_lista(request, slug_nombre_autor, lista_pk): 
    # Vista para "<str:nombre_autor>/lista-tareas/<int:lista_pk>"
    # TODO: debería ser un slug pero de momento en urls es un str
    # esto debería recibir un ID de lista
    
    try:
        lista_actual = Lista.get_lista_por_pk(pk=lista_pk)
    except Lista.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {lista_pk} no existe para el autor {slug_nombre_autor}. Revisa si el slug del autor es correcto")
    
    coleccion_tareas = Tarea.objects.filter(lista_id=lista_actual.pk)#esto está mal, debería ser por lista_id
    template = loader.get_template("listas/lista.html")
    context = {        
        "nombre_lista_actual" : lista_actual.nombre,    #Se usa en el Título
        "slug_nombre_autor": slug_nombre_autor,         #Se usa en el Subtítulo
        "coleccion_tareas": coleccion_tareas,           #TODO: esto es un <QuerySet [<Tarea: Descripción: Recoger la mesa de mi habitación (TODO). Author: saul>, <Tarea: Descripción: Recoger la ropa tendida (TODO). Author: saul>]>                
        "lista_actual_pk"   : lista_actual.pk
    }
    
    return HttpResponse(template.render(context, request))


