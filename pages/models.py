from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    #texto enrriquesido
    content = RichTextField(verbose_name="contenido")
    slug = models.CharField(unique=True,max_length=150, verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name='orden')
    visible = models.BooleanField(verbose_name="visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="creado el:")
    upgrade_at = models.DateTimeField(auto_now=True, verbose_name="actualizado el :")
    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "paginas"
    def __str__(self) -> str:
        return self.title