from django.urls import path

from .views import vista_home, vista_tareas, vista_listas

urlpatterns = [
    path("", vista_listas, name="home"), # http://127.0.0.1:8000/listas/
    path("home/", vista_home, name="home"),
    path("tareas/", vista_tareas, name="tareas"),
    path("listas/", vista_tareas, name="listas"),
]