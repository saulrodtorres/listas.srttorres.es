from django.db import models


from django.utils.text import slugify



class Tarea(models.Model):
#   Este es mi intento de INIT personalizado que no funciona porque luego hay otro pk que se genera automáticamente
#    def __init__(self):
#        self.id = contador++
#        self.descripcion = ''
#        self.estado = ''
#        self.author_id = 0
#        self.slug_descripcion = slugify(self.descripcion)
#        self.slug_author_id = slugify(self.author_id)
#        self.slug_lista_id = slugify(self.lista_id)

    descripcion = models.CharField(max_length=50)      
    author_id = models.CharField(max_length=50)
    lista_id = models.ForeignKey('Lista', on_delete=models.CASCADE, null=True, blank=True)
    slug_descripcion = models.SlugField(max_length=50, blank=True)
    slug_author_id = models.SlugField(max_length=50,blank=True)
    slug_lista_id = models.SlugField(max_length=50, blank=True)
    class Estado_tarea(models.TextChoices):
        PENDIENTE = 'Pendiente'
        COMPLETADA = 'Completada'
        INICIADA = 'Iniciada'  
    estado = models.CharField(max_length=10, choices=Estado_tarea, default=Estado_tarea.PENDIENTE) 
    @classmethod
    def crear_tarea(cls, lista_pk):
        lista = Lista.objects.get(pk=lista_pk)
        tarea = cls(lista_id = lista)
        tarea.save()
        return tarea
    
    @classmethod
    def get_tarea_por_pk(cls, pk):
        tarea = Tarea.objects.get(pk=pk)
        return tarea
    
    
    @classmethod
    def print_estado(cls):
        name_estado = cls.estado.name
        return name_estado
#    fase 2
#    fecha_creacion = models.DateTimeField(auto_now_add=True)
#    fecha_limite = models.DateTimeField(null=True, blank=True)
#    fecha_completada = models.DateTimeField(null=True, blank=True)
#    usuario_asignado = models.CharField(max_length=50, blank=True) #esto a lo mejor es un foreign key

    def __str__(self):
        tostring = self.descripcion + ' (' + self.estado + ')'
        tostring = f"Descripción: {self.descripcion} ({self.estado}). Author: {self.author_id}"
        return tostring
    

class Lista(models.Model):
    nombre = models.CharField(max_length=50)
    author_id= models.CharField(max_length=50)
    slug_nombre = models.SlugField(max_length=50, blank=True)
    slug_author_id = models.SlugField(max_length=50, blank=True)

    @classmethod
    def crear_lista(cls,nombre, author_id):#probar
        lista = cls(nombre=nombre, author_id=author_id, slug_nombre=slugify(nombre), slug_author_id=slugify(author_id))
        lista.save()
        return lista
    @classmethod
    def get_lista(cls,nombre, author_id):
        lista = Lista.objects.get(nombre=nombre, author_id=author_id)        
        return lista
    @classmethod
    def get_lista_por_pk(cls, pk):
        lista = Lista.objects.get(pk=pk)
        return lista
    @classmethod
    def get_lista_por_slug(cls, slug_nombre, slug_author_id):
        lista = Lista.objects.get(slug_nombre=slug_nombre, slug_author_id=slug_author_id)        
        return lista
    @classmethod
    def get_pk(cls):
        pk = Lista.objects.get(pk)
        return pk
    
    def __str__(self):
        return self.nombre
