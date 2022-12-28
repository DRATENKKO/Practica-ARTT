from django.contrib import admin
from .models import *
# Register your models here.


# MEMORICE


class MemoriceAdmin(admin.ModelAdmin):
    list_display = ["usuario", "acierto", "tiempo",
                    "movimientos", "timestamp"]

class Resultado_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_resultado", "id_usuario", "id_juego",
                    "resultado_1", "resultado_2", "resultado_3",
                    "resultado_4", "resultado_5","timestampp"]

class galleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "user","timestamp"]



admin.site.register(Memorice, MemoriceAdmin)
admin.site.register(Galeria)
admin.site.register(Tipo_juego)
admin.site.register(Juego)
admin.site.register(Resultado_juego,Resultado_juegoAdmin)
admin.site.register(Usuario)
admin.site.register(Tipo_usuario)
admin.site.register(Terapista)
admin.site.register(gallery,galleryAdmin)

