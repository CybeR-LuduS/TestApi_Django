from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Vehiculo, Categoria, Usuario
from .serializers import VehiculoSerializer, CategoriaSerializer, UsuarioSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    serializer = VehiculoSerializer(vehiculos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def lista_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def actualizar_vehiculo(request, patente):
    try:
        vehiculo = Vehiculo.objects.get(patenteVehiculo=patente)
    except Vehiculo.DoesNotExist:
        return Response({"message": "El vehículo no existe"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def actualizar_usuario(request, correo):
    try:
        usuario = Usuario.objects.get(correoUsuario=correo)
    except Usuario.DoesNotExist:
        return Response({"message": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        rut = usuario.rut  # Obtener el Rut del usuario
        usuario.contrasennia = rut  # Utilizar el Rut como contraseña
        usuario.save()

        return Response({"message": "Contraseña actualizada con éxito"}, status=status.HTTP_200_OK)