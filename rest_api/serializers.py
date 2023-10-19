from rest_framework import serializers
from core.models import Vehiculo, Categoria, Usuario


from rest_framework import serializers
from core.models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patenteVehiculo', 'marca', 'modelo', 'annio', 'color', 'capacidadPasajeros']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['idCategoria', 'nombre', 'descripcion']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rut', 'correo', 'contrasennia', 'nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'carrera', 'sede', 'idCategoria', 'categoria', 'isActive', 'patenteVehiculo', 'patente']