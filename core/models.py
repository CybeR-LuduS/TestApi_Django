from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name = "Id de Categoria")
    nombre = models.CharField(max_length=50, verbose_name = "Nombre de Categoria")
    descripcion = models.CharField(max_length=200, verbose_name = "Descripcion de Categoria")

    def __str__(self):
        return self.nombre

