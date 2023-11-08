from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patenteVehiculo = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name="Patente del Vehículo")
    marca = models.CharField(max_length=50, verbose_name="Marca del Vehículo")
    modelo = models.CharField(max_length=50, verbose_name="Modelo del Vehículo")
    annio = models.PositiveIntegerField(verbose_name="Annio del Vehículo")
    color = models.CharField(max_length=20, verbose_name="Color del Vehículo")
    capacidadPasajeros = models.PositiveIntegerField(verbose_name="Capacidad de Pasajeros")

    
    def __str__(self):
        texto = "({0}) {1} {2}"
        return texto.format(self.patenteVehiculo, self.marca, self.modelo)


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name = "Id de Categoria")
    nombre = models.CharField(max_length=50, verbose_name = "Nombre de Categoria")
    descripcion = models.CharField(max_length=200, verbose_name = "Descripcion de Categoria")

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, unique=True, max_length=10, verbose_name="Rut de Usuario") # Rut sin puntos y con guión
    correo = models.CharField(max_length=100, unique=True, verbose_name="Correo de Usuario")
    contrasennia = models.CharField(max_length=20, verbose_name="Contrasennia de Usuario")
    nombre = models.CharField(max_length=50, verbose_name="Primer nombre de Usuario")
    apellidoPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno de Usuario")
    apellidoMaterno = models.CharField(max_length=50, verbose_name="Apellido materno de Usuario")
    fechaNacimiento = models.CharField(max_length=10, verbose_name="Fecha de nacimiento de Usuario")
    carrera = models.CharField(max_length=100, verbose_name="Carrera de Usuario")
    sede = models.CharField(max_length=50, verbose_name="Sede de Usuario")
    
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría de Usuario") # Llave foránea, para conectar con clase Categoria
    categoria = models.CharField(max_length=50, verbose_name = "Nombre de Categoria de Usuario")

    isActive = models.BooleanField(blank=True, verbose_name="Disponibilidad de Usuario Chofer")

    patenteVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, max_length=10, blank=True, verbose_name="Patente de vehículo de Usuario chofer") # Llave foránea, para conectar con clase Vehiculo
    patente = models.CharField(max_length=10, unique=True, blank=True, verbose_name="Patente del Vehículo de Usuario Chofer")

    def __str__(self):
        texto = "({0}) {1} {2}"
        return texto.format(self.rut, self.nombre, self.apellidoPaterno)
    

class Viaje(models.Model):
    idViaje = models.AutoField(primary_key=True, verbose_name="Id de Viaje")
    sedeDuoc = models.CharField(max_length=30, verbose_name="Sede Duoc")
    rutConductor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Rut del Conductor") # Llave foránea, para conectar con clase Usuario de categoría 'Chofer'
    horaSalida = models.TimeField(verbose_name="Hora de salida")
    capacidadPasajeros = models.IntegerField(verbose_name="Capacidad de Pasajeros")
    precioPorPersona = models.IntegerField(verbose_name="Precio por Persona")
    patenteVehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, max_length=10, blank=True, verbose_name="Patente de vehículo de Usuario chofer") # Llave foránea, para conectar con clase Vehiculo
    estadoViaje = models.CharField(max_length=20, verbose_name="Estado del viaje") # Programado, En curso, Completado, Cancelado

    def __str__(self):
        texto = "({0}) ({1}) {2}"
        return texto.format(self.idViaje, self.patenteVehiculo, self.estadoViaje)



