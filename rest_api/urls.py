from django.urls import path
from rest_api.views import lista_vehiculos, lista_categorias, lista_usuarios 
from . import views

urlpatterns=[
    path('lista_vehiculos', lista_vehiculos, name="Lista Vehiculos"),
    path('lista_categorias', lista_categorias, name="Lista Categorias"),
    path('lista_usuarios', lista_usuarios, name="Lista Usuarios"),

    path('choferes-activos/', views.choferes_activos, name='choferes_activos'),
]