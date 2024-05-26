from django.urls import path

from .views import *

urlpatterns = [

    path("", vista_home, name="home"),                                                                  # http://127.0.0.1:8000/ mostrará la colección de listas de tareas
    path("home/", vista_home, name="home"),
    path("<slug:slug_nombre_autor>/lista-tareas/<int:lista_pk>", vista_lista, name="lista"),            # http://127.0.0.1:8000/saul/lista-tareas/1/tarea/1/ El autor no haría falta, bastaría con el PK
    path("<slug:slug_nombre_autor>/lista-tareas/<int:lista_pk>/tarea/<int:tarea_pk>/", vista_tarea, name="tarea"),               
                                                                                                        # habría que hacerla modificable. creo que debería agruparse por autor
    
    path("lista-tareas/nueva", vista_nueva_lista, name="nueva_lista"),                                  # http://127.0.0.1:8000/lista-tareas/nueva aquí se crea una lista con los valores por defecto

    # borrar posicion = borrar tarea con ID = PK
    # Completar tarea por posicion = Completar tarea con ID = PK
    
    
    
]