from django.contrib import admin
from .models import *
# Register your models here.


# MEMORICE


class MemoriceAdmin(admin.ModelAdmin):
    list_display = ["usuario", "acierto", "tiempo",
                    "movimientos", "timestamp"]


admin.site.register(Memorice, MemoriceAdmin)
admin.site.register(Galeria)
admin.site.register(Tipo_juego)
admin.site.register(Juego)
admin.site.register(Resultado_juego)
admin.site.register(Usuario)
admin.site.register(Tipo_usuario)
admin.site.register(Terapista)

