from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    description = models.CharField(max_length=255, verbose_name='descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    upgrate_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de actualizacion')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='titulo')
    content = RichTextField(verbose_name='contenido')
    image = models.ImageField(default='null', verbose_name='imagen', upload_to="articles")
    plublic = models.BooleanField(verbose_name='¿publicado?')
    #relacion de uno a uno
    user = models.ForeignKey(User, editable=False ,verbose_name='usuario', on_delete=models.CASCADE)
    #relacion de uno a muchos mychos articulos tienen muchas categorias
    categories = models.ManyToManyField(Category, verbose_name='categotias', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    upgrate_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de actualizacion')
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
    def __str__(self) -> str:
        return self.title