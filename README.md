# listas.srttorres.es
Listas de tareas, listas de la compra, green flags, red flags, etc




# RUN IN WINDOWS:
# Activar el virtualenvironment, que ya debe de tener instalado Django
cd .\venv_web.srttorres.es\Scripts\; Set-ExecutionPolicy Unrestricted -Scope Process; ./activate
cd ../web
python manage.py runserver



# Programa de prueba en el shell
from listas.models import *
lista_saul = Lista.crear_lista("lista saul", "saul")
tarea_1 = Tarea.crear_tarea(descripcion="Preparar folleto de excursión", author_id="saul", lista_id = lista_saul)
tarea_2 = Tarea.crear_tarea(descripcion="Editar fotos del concierto", author_id="saul", lista_id = lista_saul)

http://127.0.0.1:8000/saul/lista-tareas/lista-saul
