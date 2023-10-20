from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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
    
@api_view(['GET'])
def choferes_activos(request):
    usuarios = Usuario.objects.filter(categoria='chofer', isActive=True)
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)