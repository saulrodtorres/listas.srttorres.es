from django.urls import include, path
from . import views
from .views import *
app_name = "listas"
urlpatterns = [
    path("", views.vista_home, name="home"),                                                                  # http://127.0.0.1:8000/ mostrará la colección de listas de tareas
    path("lista-tareas/", views.nueva_lista, name="nueva_lista"),                    # http://127.0.0.1:8000/lista-tareas aquí se crea una lista de tareas
    path("lista-tareas/<int:lista_pk>", views.vista_lista, name="lista"),            # http://127.0.0.1:8000/lista-tareas/70 mostrar la lista de tareas con ID = 70
    path("lista-tareas/<int:lista_pk>/borrar", views.borrar_lista, name="borrar_lista"),            # http://127.0.0.1:8000/lista-tareas/70 mostrar la lista de tareas con ID = 70
    path("tarea/<int:tarea_pk>/", vista_tarea, name="tarea"),               
                                                                                                        # habría que hacerla modificable. creo que debería agruparse por autor
    #path('', include(('listas.urls', 'listas'), namespace='listas')), fixed by app_name
    
    # borrar posicion = borrar tarea con ID = PK
    # Completar tarea por posicion = Completar tarea con ID = PK

    #obviamente habría que pedir permisos para modificar una tarea
]

