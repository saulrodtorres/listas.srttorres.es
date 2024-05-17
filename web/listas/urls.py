from django.urls import path

from .views import *

urlpatterns = [
    path("", vista_home, name="home"), # http://127.0.0.1:8000/ mostrará la colección de listas de tareas
    path("home/", vista_home, name="home"),
    path("tarea/<int:tarea_id>/", vista_tarea, name="tarea"),#habría que hacerla modificable
    path("lista-tareas/lista1", vista_lista, name="lista"), #aquí va el ID de la lista
    path("lista-tareas/", vista_lista, name="crear_lista"), #aquí se crea una lista con los valores por defecto
    
]