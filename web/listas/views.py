from django.shortcuts import render
from django.http import Http404, HttpResponse

from django.template import loader # Para cargar plantillas de la forma 2, ahora se usa render

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *


def vista_home(request):
    # Vista para la página principal
    # TODO: leer sobre las colecciones de objetos en django

    return HttpResponse('En la vista home debería aparecer la colección de listas de tareas')

def vista_tarea(request, lista_pk, tarea_pk):
    # Vista para "<str:slug_nombre_autor>/lista-tareas/<int:slug_nombre_lista>/tarea/<str:slug_nombre_tarea>"
    # Es un formulario para editar una tarea.
    try:
        tarea_actual = Tarea.get_tarea_por_pk(pk=tarea_pk)
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {tarea_pk} no existe. Revisa si el PK de la tarea es correcta")    
    context = {                
        "tarea": tarea_actual,                          #Esto es un objeto Tarea. Solo hace falta decir tarea_pk porque eso la hace única.
    }
    #podría comprobarse que la tarea_pk está en la lista_pk   
    return render(request, "listas/tarea.html", context=context)

def nueva_lista(request):
    # Vista para guardar la nueva lista
    lista = Lista()
    lista_id = lista.pk
    lista.nombre = "La lista del Caesar"
    nueva_lista = get_object_or_404(Lista, pk=1)
    print(nueva_lista)
    try:
        nueva_lista = Lista.objects.get(pk=lista_id)
    except (KeyError, Lista.DoesNotExist):
        return render(request, 'listas/nueva_lista.html', {
            'lista': nueva_lista,
            'error_message': "No se ha podido cargar la lista",
        })
    else:
        nueva_lista.nombre = request.POST['nombre_lista'] #recojo el name del input
        nueva_lista.author_id = request.POST['autor_lista'] #esto no tiene mucho sentido, solo cuando no cambia el slug y el autor
        nueva_lista.slug_nombre = slugify(nueva_lista.nombre)
        nueva_lista.slug_author_id = slugify(nueva_lista.author_id)
        nueva_lista.save()
        return HttpResponseRedirect(reverse('listas:lista', args=(nueva_lista.pk)))


def vista_lista(request, lista_pk): 
    # Vista para "<str:nombre_autor>/lista-tareas/<int:lista_pk>"
    # Es un formulario para editar el nombre de una lista y añadir tareas a la lista    
    try:
        lista_actual = Lista.get_lista_por_pk(pk=lista_pk)
    except Lista.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {lista_pk}")    
    coleccion_tareas = Tarea.objects.filter(lista_id=lista_actual.pk)#esto está mal, debería ser por lista_id
    context = {        
        "nombre_lista_actual" : lista_actual.nombre,    #Se usa en el Título
        "coleccion_tareas": coleccion_tareas,           #TODO: esto es un <QuerySet [<Tarea: Descripción: Recoger la mesa de mi habitación (TODO). Author: saul>, <Tarea: Descripción: Recoger la ropa tendida (TODO). Author: saul>]>                
        "lista_actual_pk"   : lista_actual.pk
    }    
    return render(request, "listas/lista.html", context=context)


