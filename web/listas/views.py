from django.shortcuts import render
from django.http import Http404, HttpResponse

from django.template import loader # Para cargar plantillas de la forma 2, ahora se usa render

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *


def vista_home(request):
    # Vista para la página principal
    # Mostrar todas las listas de tareas
    
    coleccion_listas = Lista.objects.all() #Esto es un <QuerySet [<Lista: Lista de tareas de saul>, <Lista: Lista de la compra>]...etc> 
    context = { 
        "coleccion_listas"       : coleccion_listas,
    }
    return render(request, "listas/index.html", context=context)
def nueva_tarea(request, lista_pk):
    # Vista para enviar un formulario para crear una nueva tarea
    tarea = Tarea.crear_tarea(lista_pk)
    context = { 
        "tarea"      : tarea,
        "lista"      : tarea.lista_id,
    }
    return render(request, "listas/nueva_tarea.html", context=context)

def vista_tarea(request, tarea_pk):
    # Vista para "<str:slug_nombre_autor>/lista-tareas/<int:slug_nombre_lista>/tarea/<str:slug_nombre_tarea>"
    # Es un formulario para editar una tarea.
    try:
        tarea_actual = Tarea.get_tarea_por_pk(pk=tarea_pk)
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {tarea_pk} no existe. Revisa si el PK de la tarea es correcta")    
    try:
        lista_actual = Lista.objects.get(pk=tarea_actual.lista_id.pk)
    except Lista.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {tarea_actual.lista_id.pk} no existe. Revisa si el PK de la lista es correcta")
    try:
        #Aquí lo que querría es saber si existe un POST o si es un GET.
        tarea_actual.descripcion = request.POST.get('descripcion_tarea', tarea_actual.descripcion) #Si no existe en el POST, devuelve la que había recogido en tarea_actual
        tarea_actual.author_id = request.POST.get('autor_tarea', tarea_actual.author_id) 
        tarea_actual.estado = request.POST.get('estado_tarea', tarea_actual.estado)
        tarea_actual.slug_descripcion = slugify(tarea_actual.descripcion)
        tarea_actual.slug_author_id = slugify(tarea_actual.author_id)
        tarea_actual.save()
    except:
        pass


    context = {                
        "tarea": tarea_actual,                          #Esto es un objeto Tarea. Solo hace falta decir tarea_pk porque eso la hace única.
        "lista": lista_actual,                          #Esto es un objeto Lista. Solo hace falta decir lista_pk porque eso la hace única.
    }
    #podría comprobarse que la tarea_pk está en la lista_pk   
    return render(request, "listas/tarea.html", context=context)
def borrar_tarea(request, tarea_pk):
    # Vista para borrar una tarea
    try:
        tarea_actual = Tarea.objects.get(pk=tarea_pk)
    except Tarea.DoesNotExist:
        raise Http404(f"Lo siento, pero la tarea con PK {tarea_pk} no existe. Revisa si el PK de la tarea es correcta")    
    tarea_actual.delete()
    return HttpResponseRedirect(reverse('listas:lista', args=(tarea_actual.lista_id.pk,))) #Redirige a la página principal pero debería redirigir a la lista de la que se ha borrado la tarea
    #return HttpResponseRedirect(reverse('listas:lista', tarea_actual.lista_id.pk )) #Redirige a la página principal pero debería redirigir a la lista de la que se ha borrado la tarea

def nueva_lista(request):
    # Vista para enviar un formulario para crear una nueva lista
    lista = Lista()
    lista.save()
    context = { 
        "lista"       : lista,
    }
    return render(request, "listas/nueva_lista.html", context=context)  

def vista_lista(request, lista_pk): 
    # Vista para "lista-tareas/<int:lista_pk>" y para recibir la lista nada más crearla
    # Tratamiento si ya está creada
    try:
        lista_actual = Lista.objects.get(pk=lista_pk)
    except Lista.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {lista_pk}")    
    try:
        #Aquí lo que querría es saber si existe un POST o si es un GET.
        lista_actual.nombre = request.POST.get('nombre_lista', lista_actual.nombre) #Si no existe, devuelve la que había recogido en lista_actual
        lista_actual.author_id = request.POST.get('autor_lista', lista_actual.author_id) 
        lista_actual.slug_nombre = slugify(lista_actual.nombre)
        lista_actual.slug_author_id = slugify(lista_actual.author_id)
        lista_actual.save()
    except:
        pass

    #Es muy posible que no exista coleccion_tareas para una lista recién creada
    coleccion_tareas = Tarea.objects.filter(lista_id=lista_actual.pk)#esto está mal, debería ser por lista_id
    context = {        
        "nombre_lista_actual" : lista_actual.nombre,    #Se usa en el Título
        "coleccion_tareas": coleccion_tareas,           #TODO: esto es un <QuerySet [<Tarea: Descripción: Recoger la mesa de mi habitación (TODO). Author: saul>, <Tarea: Descripción: Recoger la ropa tendida (TODO). Author: saul>]>                
        "lista"   : lista_actual
    }
    
    return render(request, "listas/lista.html", context=context)
    #return HttpResponseRedirect(reverse('listas:lista', args=(nueva_lista.pk,)))#TODO:Aprender a usarlo

def borrar_lista(request, lista_pk):
    # Vista para borrar una lista
    try:
        lista_actual = Lista.objects.get(pk=lista_pk)
    except Lista.DoesNotExist:
        raise Http404(f"Lo siento, pero la lista con PK {lista_pk}")    
    lista_actual.delete()
    return HttpResponseRedirect(reverse('listas:home')) #Redirige a la página principal
    
