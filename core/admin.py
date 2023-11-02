from django.contrib import admin
from .models import Vehiculo, Categoria, Usuario, Viaje

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Viaje)
