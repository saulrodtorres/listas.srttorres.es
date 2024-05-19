from django.urls import path

from .views import *

urlpatterns = [
    path("", vista_home, name="home"),                                      # http://127.0.0.1:8000/ mostrará la colección de listas de tareas
    path("home/", vista_home, name="home"),
    path("tarea/<str:nombre_autor>/<str:nombre_lista>/<str:nombre_tarea>/", vista_tarea, name="tarea"),               
                                                                            # habría que hacerla modificable. creo que debería agruparse por autor
    
    path("lista-tareas/nueva", vista_nueva_lista, name="nueva_lista"),      # http://127.0.0.1:8000/lista-tareas/nueva aquí se crea una lista con los valores por defecto
    path("lista-tareas/<str:nombre_lista>", vista_lista, name="lista"),     # aquí va el ID de la lista
    
    
]