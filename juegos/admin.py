from django.contrib import admin
from .models import *
class Sopa_letrasAdmin(admin.ModelAdmin):
    list_display = ["id_sopa","user","pregunta_sopa", "word","direction", "start"]

class TriviaAdmin(admin.ModelAdmin):
    list_display = ["id_trivia","user", "ordinal","pregunta_trivia", "respuesta_trivia"]

class JuegoAdmin(admin.ModelAdmin):
    list_display = ["id","descripcion", "id_tipo_juego"]

#SOPALETRAS
admin.site.register(Sopa_letra,Sopa_letrasAdmin)
#TRIVIA
admin.site.register(Trivia,TriviaAdmin)
#JUEGO
admin.site.register(Juego,JuegoAdmin)