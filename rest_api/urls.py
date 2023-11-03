from django.urls import path
from rest_api.views import lista_vehiculos, lista_categorias, lista_usuarios, choferes_activos, lista_viajes
 
from . import views

urlpatterns=[
    path('lista_vehiculos', lista_vehiculos, name="Lista Vehiculos"),
    path('lista_categorias', lista_categorias, name="Lista Categorias"),
    path('lista_usuarios', lista_usuarios, name="Lista Usuarios"),

    path('choferes_activos', choferes_activos, name="Choferes Activos"),

    path('lista_viajes', lista_viajes, name="Lista Viajes")
]