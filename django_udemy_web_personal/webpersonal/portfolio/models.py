from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to = "projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha modificado")
    URLmore = models.URLField(verbose_name="Web site:", null=True, blank=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title