from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Patente del Vehículo")
    marca = models.CharField(max_length=50, verbose_name="Marca del Vehículo")
    modelo = models.CharField(max_length=50, verbose_name="Modelo del Vehículo")
    año = models.PositiveIntegerField(verbose_name="Año del Vehículo")
    color = models.CharField(max_length=20, verbose_name="Color del Vehículo")
    capacidad_pasajeros = models.PositiveIntegerField(verbose_name="Capacidad de Pasajeros")

    
    def __str__(self):
        texto = "({0}) {1} {2}"
        return texto.format(self.patente, self.marca, self.modelo)


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name = "Id de Categoria")
    nombre = models.CharField(max_length=50, verbose_name = "Nombre de Categoria")
    descripcion = models.CharField(max_length=200, verbose_name = "Descripcion de Categoria")

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, unique=True, max_length=10, verbose_name="Rut de Usuario") # Rut sin puntos y con guión
    nombre = models.CharField(max_length=50, verbose_name="Primer nombre de Usuario")
    apellidoPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno de Usuario")
    apellidoMaterno = models.CharField(max_length=50, verbose_name="Apellido materno de Usuario")
    fechaNacimiento = models.CharField(max_length=10, verbose_name="Fecha de nacimiento de Usuario")
    carrera = models.CharField(max_length=100, verbose_name="Carrera de Usuario")
    sede = models.CharField(max_length=50, verbose_name="Sede de Usuario")
    
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría de Usuario") # Llave foránea, para conectar con clase Categoria

    isActive = models.BooleanField(blank=True, null=True, verbose_name="Disponibilidad de Usuario Chofer")

    patenteVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, max_length=10, blank=True, null=True, verbose_name="Patente de vehículo de Usuario chofer") # Llave foránea, para conectar con clase Vehiculo

    def __str__(self):
        texto = "({0}) {1} {2}"
        return texto.format(self.rut, self.nombre, self.apellidoPaterno)
    




