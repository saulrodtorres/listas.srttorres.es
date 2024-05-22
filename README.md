# listas.srttorres.es
Listas de tareas, listas de la compra, green flags, red flags, etc




# RUN IN WINDOWS:


Set-ExecutionPolicy Unrestricted -Scope Process
./activate
cd ../web
python manage.py runserver



# Programa de prueba en el shell
from listas.models import *
lista_saul = Lista.crear_lista("lista saul", "saul")
tarea_1 = Tarea.crear_tarea(descripcion="Recoger la mesa de mi habitación", author_id="saul", lista_id = lista_saul)
tarea_2 = Tarea.crear_tarea(descripcion="Recoger la ropa tendida", author_id="saul", lista_id = lista_saul)

http://127.0.0.1:8000/saul/lista-tareas/lista-saul
