from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField( verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.name

class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ["-created"]
