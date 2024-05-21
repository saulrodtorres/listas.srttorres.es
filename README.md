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

