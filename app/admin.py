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

class TerapistaAdmin(admin.ModelAdmin):
    list_display = ["id_enfermera", "rut_enfermera", "nombre_enfermera", "apellido_enfermera", "direccion_enfermera", "correo_enfermera", "telefono_enfermera","whatsapp_enfermera","telegram_enfermera","celular_enfermera"]

class RegionAdmin(admin.ModelAdmin):
    list_display = ["id_region", "nombre_region"]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["id_provincia", "nombre_provincia", "id_region"]

class ComunaAdmin(admin.ModelAdmin):
    list_display = ["id_comuna", "nombre_comuna", "id_provincia"]

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ["id_institucion", "nombre_institucion", "descripcion_institucion", "id_comuna"]

class HipertensionAdmin(admin.ModelAdmin):
    list_display = ["id_hipertension", "estado_hipertension"]

class DiabetesAdmin(admin.ModelAdmin):
    list_display = ["id_diabetes", "tipo_diabetes"]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["id_paciente", "rut_paciente", "telegram_paciente", "diabetes_id", "hipertension", "user", "paciente_familiar","whatsapp_paciente","celular_paciente"]

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ["id_familiar", "rut_familiar", "user"]

class Familiar_pacienteAdmin(admin.ModelAdmin):
    list_display = ["Paciente","Familiar","parentesco"]

class IntensidadAdmin(admin.ModelAdmin):
    list_display = ["id_intensidad", "timestamp","url_archivo_intensidad","intensidad","mindb","maxdb","comentario","Paciente"]


class App_documentoAdmin(admin.ModelAdmin):
    list_display = ["id_app_documento", "titulo", "documento","descripcion","qr"]

class VocalizacionAdmin(admin.ModelAdmin):
    list_display = ["id_vocalizacion", "timestamp","url_archivo_vocalizacion","duracion","bpminute","bpmeasure","comentario","Paciente"]

class App_enfermera_neurologoAdmin(admin.ModelAdmin):
    list_display = ["id_app_enfermera_neurologo", "username_enfermera", "username_neurologo"]

class App_enfermera_pacienteAdmin(admin.ModelAdmin):
    list_display = ["id_app_enfermera_paciente", "username_enfermera", "username_paciente"]

class App_tipo_terapiaAdmin(admin.ModelAdmin):
    list_display = ["id_app_tipo_terapia", "descripcion"]

class TerapiaAdmin(admin.ModelAdmin):
    list_display = ["id_terapia", "horarios","fonoaudiologo_id","paciente_id","id_app_tipo_terapia"]

class Recordatorio_terapiaAdmin(admin.ModelAdmin):
    list_display = ["id_recordatorio_terapia", "hora_recordatorio","receta_id","id_terapia"]

class AudioAdmin(admin.ModelAdmin):
    list_display = ["id_audio", "timestamp","url_archivo_audio","jitter_ppq5","jitter_rap","maximum_pitch","error_jitter_ppq5","error_jitter_rap","error_maximum_pitch","jitter_ppq5_IA","jitter_rap_IA","maximum_pitch_IA","error_jitter_ppq5_IA","error_jitter_rap_IA","error_maximum_pitch_IA","id_paciente"]

class Profesional_saludAdmin(admin.ModelAdmin):
    list_display = ["id_profesional_salud", "rut_profesional_salud", "id_institucion", "user"]

class Profesional_pacienteAdmin(admin.ModelAdmin):
    list_display = ["id_profesional_paciente", "descripcion", "id_profesional_salud","id_paciente"]

class Tipo_parentescoAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_parentesco", "parentesco"]

#TIPO PARENTESCO
admin.site.register(Tipo_parentesco,Tipo_parentescoAdmin)
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
#TERAPISTA
admin.site.register(Terapista,TerapistaAdmin)
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
#INSTITUCION
admin.site.register(Institucion,InstitucionAdmin)
#PACIENTE
#FAMILIAR
admin.site.register(Familiar,FamiliarAdmin)
#FAMILIAR PACIENTE
admin.site.register(Familiar_paciente,Familiar_pacienteAdmin)
#INTENSIDAD
admin.site.register(Intensidad,IntensidadAdmin)
#APP DOCUMENTO
admin.site.register(App_documento,App_documentoAdmin)
#VOCALIZACION
admin.site.register(Vocalizacion,VocalizacionAdmin)
#APP ENFERMERA NEUROLOGO
admin.site.register(App_enfermera_neurologo,App_enfermera_neurologoAdmin)
#APP ENFERMERA PACIENTE
admin.site.register(App_enfermera_paciente,App_enfermera_pacienteAdmin)
#APP TIPO TERAPIA
admin.site.register(App_tipo_terapia,App_tipo_terapiaAdmin)
#TERAPIA
admin.site.register(Terapia,TerapiaAdmin)
#RECORDATORIO TERAPIA
admin.site.register(Recordatorio_terapia,Recordatorio_terapiaAdmin)
#AUDIO
admin.site.register(Audio,AudioAdmin)
#PROFESIONAL SALUD
admin.site.register(Profesional_salud,Profesional_saludAdmin)
#PROFESIONAL PACIENTE
admin.site.register(Profesional_paciente,Profesional_pacienteAdmin)
#SOPA DE LETRAS
admin.site.register(Sopa_letras,Sopa_letrasAdmin)