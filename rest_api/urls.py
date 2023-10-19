from django.urls import path
from rest_api.views import lista_vehiculos, lista_categorias, lista_usuarios 

urlpatterns=[
    path('lista_vehiculos', lista_vehiculos, name="Lista Vehiculos"),
    path('lista_categorias', lista_categorias, name="Lista Categorias"),
    path('lista_usuarios', lista_usuarios, name="Lista Usuarios"),
]