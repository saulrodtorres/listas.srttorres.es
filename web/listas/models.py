from django.db import models

# Create your models here.

from django.utils.text import slugify



class Tarea(models.Model):

#    def __init__(self):
#        self.id = 1000
#        self.descripcion = ''
#        self.estado = ''
#        self.author_id = 0
    descripcion = models.CharField(max_length=50)  
    class estado_tarea(models.TextChoices):
        PENDIENTE = 'TODO', 'Pendiente'
        COMPLETADA = 'DONE', 'Completada'
        INICIADA = 'INIT', 'Iniciada'  
    estado = models.CharField(max_length=4, choices=estado_tarea.choices, default=estado_tarea.PENDIENTE)    
    author_id = models.IntegerField(null=True, blank=True)
    lista_id = models.ForeignKey('Lista', on_delete=models.CASCADE, null=True, blank=True)
#    fase 2
#    fecha_creacion = models.DateTimeField(auto_now_add=True)
#    fecha_limite = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        tostring = self.descripcion + ' (' + self.estado + ')'
        tostring = f"Descripción: {self.descripcion} ({self.estado}). Author: {self.author_id}"
        return tostring
    

class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    author_id= models.CharField(max_length=50)
    
    @classmethod
    def crear_lista(cls,nombre, author_id):#probar
        lista = cls(nombre=nombre, author_id=author_id)
        lista.save()
        return lista
    
    def __str__(self):
        return self.nombre