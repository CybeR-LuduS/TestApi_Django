from rest_framework import serializers
from core.models import Vehiculo, Categoria, Usuario, Viaje


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


class ViajeSerializer(serializers.ModelSerializer):
    patenteVehiculo = VehiculoSerializer()  # Usar un serializador anidado para el vehículo
    
    class Meta:
        model = Viaje
        fields = ['idViaje', 'sedeDuoc', 'rutConductor', 'horaSalida', 'capacidadPasajeros', 'precioPorPersona', 'patenteVehiculo', 'estadoViaje']