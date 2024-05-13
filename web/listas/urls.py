from django.urls import path

from .views import vista_home, vista_tarea, vista_listas

urlpatterns = [
    path("", vista_listas, name="home"), # http://127.0.0.1:8000/listas/
    path("home/", vista_home, name="home"),
    path("tarea/", vista_tarea, name="tarea"),
    path("l/", vista_tarea, name="listas"), #aquí va el ID de la lista
]