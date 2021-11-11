from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ['-created']

    def __str__(self):
        return self.name
class Post(models.Model):

    STATUS = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    )
    Tamanio = (
        ('pequeño', 'pequeño'),
        ('mediano', 'mediano'),
        ('grande', 'grande'),
    )
    Cast = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    sex = (
        ('macho', 'macho'),
        ('hembra', 'hembra'),
    )

    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    resumen = models.TextField(verbose_name="Resumen", null=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación", default= datetime.now())
    image = models.ImageField(verbose_name="Imagen", upload_to="galeria", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición") 
    sexo = models.CharField(max_length=200, null=True, choices=sex, verbose_name="Sexo")
    edad = models.IntegerField( null=True, blank=True,verbose_name="Edad")
    energia = models.CharField(max_length=200, null=True, choices=STATUS,verbose_name="Energía")
    tamanio = models.CharField(max_length=200, null=True, choices=Tamanio,verbose_name="Tamaño")
    castrado = models.CharField(max_length=200, null=True, choices=Cast,verbose_name="Esterilizado")
    contacto = models.CharField(max_length=200, null=True,default='https://wa.me/59173091061')
    refugio = models.CharField(max_length=200, null=True,)
    facebook = models.CharField(max_length=200, null=True,)
    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
        ordering = ['-created']

    def __str__(self):
        return self.title
