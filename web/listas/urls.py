from django.urls import path

from .views import vista_home, vista_tarea, vista_lista

urlpatterns = [
    path("", vista_home, name="home"), # http://127.0.0.1:8000/ mostrará la colección de listas de tareas
    path("home/", vista_home, name="home"),
    path("tarea/<int:tarea_id>/", vista_tarea, name="tarea"),
    path("lista-tareas/<slug:slug>", vista_lista, name="listas"), #aquí va el ID de la lista
]