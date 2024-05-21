from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import loader # Para cargar plantillas


from .models import *


def vista_home(request):
    # Vista para la página principal
    # TODO: leer sobre las colecciones de objetos en django

    return HttpResponse('En la vista home debería aparecer la colección de listas de tareas')

def vista_tarea(request, slug_nombre_autor, slug_nombre_lista, slug_nombre_tarea):
    # Vista para "<str:slug_nombre_autor>/lista-tareas/<str:slug_nombre_lista>/tarea/<str:slug_nombre_tarea>"
    # TODO: tratamiento slug_nombre_autor
    # TODO: tratamiento slug_nombre_lista
    # TODO: tratamiento slug_nombre_tarea
    # TODO: esto no tiene por qué ser único, pero sí debería ser único el author también

    try:
        tarea_actual = Tarea.objects.get(slug_descripcion=slug_nombre_tarea, slug_author_id=slug_nombre_autor, slug_lista_id=slug_nombre_lista) 
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con el slug {slug_nombre_lista} para el autor no existe para el autor {slug_nombre_autor}. Revisa si el ID es correcto")
    
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
    """ % (tarea_actual.descripcion, tarea_actual.estado)
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

def vista_lista(request, slug_nombre_autor, slug_nombre_lista): 
    # Vista para "<str:nombre_autor>/lista-tareas/<str:nombre_lista>"
    # TODO: debería ser un slug pero de momento en urls es un str
    # esto debería recibir un ID de lista
    
    #lista_actual = Lista.objects.get(descripcion=nombre_lista, author_id=nombre_autor)# TODO: esto no tiene por qué ser único, pero sí debería ser único el author también        
    lista_actual = Lista.crear_lista(nombre=slug_nombre_lista, author_id=slug_nombre_autor)
    #ESTA ESTA MAL. AQUÍ NO HAY QUE CREAR LISTA

    coleccion_tareas = Tarea.objects.filter(id=lista_actual.id)
    template = loader.get_template("listas/index.html")
    context = {
        "slug_nombre_lista": slug_nombre_lista, # "slug_nombre_lista": "nombre_lista
        "slug_nombre_autor": slug_nombre_autor,
        "coleccion de tareas": coleccion_tareas,
        "nombre_lista_actual" : lista_actual.nombre
    }
    
    ########### old way
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
    #return http_response###############

    return HttpResponse(template.render(context, request))

