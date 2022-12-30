from django.contrib import admin
from .models import *
# Register your models here.

class Resultado_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_resultado", "id_juego",
                    "resultado_1", "resultado_2", "resultado_3",
                    "resultado_4", "resultado_5","timestampp"]

class galleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "user","timestamp"]

class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_usuario", "nombre_tipo_usuario", "descripcion"]

class JuegoAdmin(admin.ModelAdmin):
    list_display = ["id", "descripcion", "id_tipo_juego"]

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username',  'email', 'id_telegram']


class Tipo_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_juego", "nombre_juego"]

admin.site.register(Tipo_juego,Tipo_juegoAdmin)
admin.site.register(Juego,JuegoAdmin)
admin.site.register(Resultado_juego,Resultado_juegoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Tipo_usuario,Tipo_usuarioAdmin)
admin.site.register(Terapista)
admin.site.register(gallery,galleryAdmin)

