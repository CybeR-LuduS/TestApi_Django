# Generated by Django 4.1.12 on 2023-10-19 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Patente del Vehículo')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca del Vehículo')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo del Vehículo')),
                ('annio', models.PositiveIntegerField(verbose_name='Annio del Vehículo')),
                ('color', models.CharField(max_length=20, verbose_name='Color del Vehículo')),
                ('capacidadPasajeros', models.PositiveIntegerField(verbose_name='Capacidad de Pasajeros')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Rut de Usuario')),
                ('correo', models.CharField(max_length=100, unique=True, verbose_name='Correo de Usuario')),
                ('contrasennia', models.CharField(max_length=20, verbose_name='Contrasennia de Usuario')),
                ('nombre', models.CharField(max_length=50, verbose_name='Primer nombre de Usuario')),
                ('apellidoPaterno', models.CharField(max_length=50, verbose_name='Apellido paterno de Usuario')),
                ('apellidoMaterno', models.CharField(max_length=50, verbose_name='Apellido materno de Usuario')),
                ('fechaNacimiento', models.CharField(max_length=10, verbose_name='Fecha de nacimiento de Usuario')),
                ('carrera', models.CharField(max_length=100, verbose_name='Carrera de Usuario')),
                ('sede', models.CharField(max_length=50, verbose_name='Sede de Usuario')),
                ('isActive', models.BooleanField(blank=True, verbose_name='Disponibilidad de Usuario Chofer')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria', verbose_name='Categoría de Usuario')),
                ('patenteVehiculo', models.ForeignKey(blank=True, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo', verbose_name='Patente de vehículo de Usuario chofer')),
            ],
        ),
    ]
