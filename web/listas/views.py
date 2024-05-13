from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista_home(request):
    return HttpResponse('Hola, soy la vista home para home/ y para /')

def vista_tareas(request):
    return HttpResponse('Hola, soy la vista tareas')

def vista_listas(request):
    return HttpResponse('Hola, soy la vista listas')