from django.contrib import admin
from .models import Juego, Categoria, Desarrollador

# Register your models here.

admin.site.register(Juego)
admin.site.register(Categoria)
admin.site.register(Desarrollador)
