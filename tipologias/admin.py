from django.contrib import admin
from .models import *
# Register your models here.
class Tipo_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_juego", "nombre_juego"]

class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_usuario", "nombre_tipo_usuario", "descripcion"]

class ComunaAdmin(admin.ModelAdmin):
    list_display = ["id_comuna", "nombre_comuna", ]

class RegionAdmin(admin.ModelAdmin):
    list_display = ["id_region", "nombre_region", ]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["id_provincia", "nombre_provincia", "id_region"]

#REGION
admin.site.register(Region,RegionAdmin)
#PROVINCIA
admin.site.register(Provincia,ProvinciaAdmin)
#COMUNA
admin.site.register(Comuna,ComunaAdmin)
#TIPO DE JUEGO
admin.site.register(Tipo_juego,Tipo_juegoAdmin)
#TIPO USUARIO
admin.site.register(Tipo_usuario,Tipo_usuarioAdmin)