from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion = models.CharField(max_length=50)
    class estado_tarea(models.TextChoices):
        PENDIENTE = 'TODO', 'Pendiente'
        COMPLETADA = 'DONE', 'Completada'
        INICIADA = 'INIT', 'Iniciada'
    estado = models.CharField(max_length=4, choices=estado_tarea.choices, default=estado_tarea.PENDIENTE)    
    author_id = models.IntegerField(null=True, blank=True)

#    fase 2
#    fecha_creacion = models.DateTimeField(auto_now_add=True)
#    fecha_limite = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre + ' (' + self.estado + ')'