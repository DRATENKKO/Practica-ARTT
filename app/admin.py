from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *

class UserAdmin(BaseUserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserCreationForm
    fieldsets = (
        ('User Profile', {'fields': ('username','Tipo_usuario', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion','id_comuna', 'password' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','Tipo_usuario', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion','id_comuna', 'password'),
            
        }),
    )
    list_display = ("username","id", "email", "first_name", "last_name", "is_staff")


class Resultado_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_resultado","id_usuario", "id_juego",
                    "resultado_1", "resultado_2", "resultado_3",
                    "resultado_4", "resultado_5","timestampp"]

class galleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "user","timestamp"]

class Tipo_usuarioAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_usuario", "nombre_tipo_usuario", "descripcion"]

class JuegoAdmin(admin.ModelAdmin):
    list_display = ["id", "descripcion", "id_tipo_juego"]

class Tipo_juegoAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_juego", "nombre_juego"]

class TriviaAdmin(admin.ModelAdmin):
    list_display = ["id_trivia","user", "ordinal","pregunta_trivia", "respuesta_trivia"]

class Sopa_letrasAdmin(admin.ModelAdmin):
    list_display = ["id_sopa","user","pregunta_sopa", "word","direction", "start"]

class RegionAdmin(admin.ModelAdmin):
    list_display = ["id_region", "nombre_region"]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["id_provincia", "nombre_provincia", "id_region"]

class ComunaAdmin(admin.ModelAdmin):
    list_display = ["id_comuna", "nombre_comuna", "id_provincia"]

class App_documentoAdmin(admin.ModelAdmin):
    list_display = ["id_app_documento", "titulo", "documento","descripcion","qr"]

class VocalizacionAdmin(admin.ModelAdmin):
    list_display = ["id_vocalizacion", "timestamp","url_archivo_vocalizacion","duracion","bpminute","bpmeasure","comentario","Paciente"]

class AudioAdmin(admin.ModelAdmin):
    list_display = ["id_audio", "timestamp","url_archivo_audio","jitter_ppq5","jitter_rap","maximum_pitch","error_jitter_ppq5","error_jitter_rap","error_maximum_pitch","jitter_ppq5_IA","jitter_rap_IA","maximum_pitch_IA","error_jitter_ppq5_IA","error_jitter_rap_IA","error_maximum_pitch_IA","id_paciente"]

#TIPO JUEGO
admin.site.register(Tipo_juego,Tipo_juegoAdmin)
#JUEGO
admin.site.register(Juego,JuegoAdmin)
#RESULTADO JUEGO
admin.site.register(Resultado_juego,Resultado_juegoAdmin)
#USUARIO
admin.site.register(Usuario,UserAdmin)
#TIPO USUARIO
admin.site.register(Tipo_usuario,Tipo_usuarioAdmin)
#GALLERY
admin.site.register(gallery,galleryAdmin)
#TRIVIA
admin.site.register(Trivia,TriviaAdmin)
#REGION
admin.site.register(Region,RegionAdmin)
#PROVINCIA
admin.site.register(Provincia,ProvinciaAdmin)
#COMUNA
admin.site.register(Comuna,ComunaAdmin)
#APP DOCUMENTO
admin.site.register(App_documento,App_documentoAdmin)
#VOCALIZACION
admin.site.register(Vocalizacion,VocalizacionAdmin)
#AUDIO
admin.site.register(Audio,AudioAdmin)
#SOPA DE LETRAS
admin.site.register(Sopa_letras,Sopa_letrasAdmin)