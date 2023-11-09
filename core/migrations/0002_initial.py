# Generated by Django 4.1.12 on 2023-11-09 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Rut de Usuario')),
                ('correo', models.CharField(max_length=100, unique=True, verbose_name='Correo de Usuario')),
                ('contrasennia', models.CharField(max_length=20, verbose_name='Contrasennia de Usuario')),
                ('nombre', models.CharField(max_length=50, verbose_name='Primer nombre de Usuario')),
                ('apellidoPaterno', models.CharField(max_length=50, verbose_name='Apellido paterno de Usuario')),
                ('apellidoMaterno', models.CharField(max_length=50, verbose_name='Apellido materno de Usuario')),
                ('carrera', models.CharField(max_length=100, verbose_name='Carrera de Usuario')),
                ('sede', models.CharField(max_length=50, verbose_name='Sede de Usuario')),
                ('categoria', models.CharField(max_length=50, verbose_name='Nombre de Categoria de Usuario')),
                ('patenteVehiculo', models.CharField(blank=True, max_length=10, verbose_name='Patente del Vehículo de Usuario Chofer')),
                ('marcaVehiculo', models.CharField(blank=True, max_length=50, verbose_name='Marca del Vehículo')),
                ('modeloVehiculo', models.CharField(blank=True, max_length=50, verbose_name='Modelo del Vehículo')),
                ('colorVehiculo', models.CharField(blank=True, max_length=20, verbose_name='Color del Vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=30, verbose_name='Sede Duoc')),
                ('rut', models.CharField(max_length=10, unique=True, verbose_name='Rut de Usuario Chofer')),
                ('horaSalida', models.TimeField(verbose_name='Hora de salida')),
                ('capacidadPasajeros', models.IntegerField(verbose_name='Capacidad de Pasajeros')),
                ('precioPorPersona', models.IntegerField(verbose_name='Precio por Persona')),
                ('estadoViaje', models.CharField(max_length=20, verbose_name='Estado del viaje')),
                ('patenteVehiculo', models.CharField(blank=True, max_length=10, verbose_name='Patente del Vehículo de Usuario Chofer')),
                ('marcaVehiculo', models.CharField(blank=True, max_length=50, verbose_name='Marca del Vehículo')),
                ('modeloVehiculo', models.CharField(blank=True, max_length=50, verbose_name='Modelo del Vehículo')),
                ('colorVehiculo', models.CharField(blank=True, max_length=20, verbose_name='Color del Vehículo')),
                ('correoChofer', models.CharField(max_length=50, verbose_name='Correo de Usuario Chofer')),
            ],
        ),
    ]