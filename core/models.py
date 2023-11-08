from django.db import models

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, unique=True, max_length=10, verbose_name="Rut de Usuario") # Rut sin puntos y con guión
    correo = models.CharField(max_length=100, unique=True, verbose_name="Correo de Usuario")
    contrasennia = models.CharField(max_length=20, verbose_name="Contrasennia de Usuario")
    nombre = models.CharField(max_length=50, verbose_name="Primer nombre de Usuario")
    apellidoPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno de Usuario")
    apellidoMaterno = models.CharField(max_length=50, verbose_name="Apellido materno de Usuario")
    carrera = models.CharField(max_length=100, verbose_name="Carrera de Usuario")
    sede = models.CharField(max_length=50, verbose_name="Sede de Usuario")
    
    categoria = models.CharField(max_length=50, verbose_name = "Nombre de Categoria de Usuario")
    patenteVehiculo = models.CharField(max_length=10, blank=True, verbose_name="Patente del Vehículo de Usuario Chofer")
    marcaVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Marca del Vehículo")
    modeloVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Modelo del Vehículo")
    colorVehiculo = models.CharField(max_length=20, blank=True, verbose_name="Color del Vehículo")


    def __str__(self):
        texto = "({0}) {1} {2} {3}"
        return texto.format(self.rut, self.categoria, self.nombre, self.apellidoPaterno)
    

class Viaje(models.Model):
    idViaje = models.AutoField(primary_key=True, verbose_name="Id de Viaje")
    sede = models.CharField(max_length=30, verbose_name="Sede Duoc")
    rut = models.CharField(unique=True, max_length=10, verbose_name="Rut de Usuario")
    horaSalida = models.TimeField(verbose_name="Hora de salida")
    capacidadPasajeros = models.IntegerField(verbose_name="Capacidad de Pasajeros")
    precioPorPersona = models.IntegerField(verbose_name="Precio por Persona")
    estadoViaje = models.CharField(max_length=20, verbose_name="Estado del viaje") # Programado, En curso, Completado, Cancelado

    patenteVehiculo = models.CharField(max_length=10, blank=True, verbose_name="Patente del Vehículo de Usuario Chofer")
    marcaVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Marca del Vehículo")
    modeloVehiculo = models.CharField(max_length=50, blank=True, verbose_name="Modelo del Vehículo")
    colorVehiculo = models.CharField(max_length=20, blank=True, verbose_name="Color del Vehículo")
    
    def __str__(self):
        texto = "({0}) ({1}) {2}"
        return texto.format(self.idViaje, self.patenteVehiculo, self.estadoViaje)



