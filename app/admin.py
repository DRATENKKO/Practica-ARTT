from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
# Register your models here.
class UserAdmin(BaseUserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserCreationForm
    fieldsets = (
        ('User Profile', {'fields': ('username', 'password', 'email','id_telegram' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion','id_comuna', 'password'),
        }),
    )


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

class TriviaAdmin(admin.ModelAdmin):
    list_display = ["id_trivia", "ordinal","pregunta_trivia", "respuesta_trivia","user"]

class Sopa_letrasAdmin(admin.ModelAdmin):
    list_display = ["id_sopa","pregunta_sopa", "word","direction", "start","user"]

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
    list_display = ["id_familiar_paciente", "id_familiar", "id_paciente","parentesco"]

class IntensidadAdmin(admin.ModelAdmin):
    list_display = ["id_intensidad", "timestamp","url_archivo_intensidad","intensidad","mindb","maxdb","comentario","Paciente"]

class Paciente_documentoAdmin(admin.ModelAdmin):
    list_display = ["id_paciente_documento", "autorizado", "timestamp","documento_id","id_paciente"]

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
admin.site.register(Tipo_juego,Tipo_juegoAdmin)
admin.site.register(Juego,JuegoAdmin)
admin.site.register(Resultado_juego,Resultado_juegoAdmin)
admin.site.register(Usuario,UserAdmin)
admin.site.register(Tipo_usuario,Tipo_usuarioAdmin)
admin.site.register(Terapista,TerapistaAdmin)
admin.site.register(gallery,galleryAdmin)
admin.site.register(Trivia,TriviaAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Comuna,ComunaAdmin)
admin.site.register(Institucion,InstitucionAdmin)
admin.site.register(Hipertension,HipertensionAdmin)
admin.site.register(Diabetes,DiabetesAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Familiar,FamiliarAdmin)
admin.site.register(Familiar_paciente,Familiar_pacienteAdmin)
admin.site.register(Intensidad,IntensidadAdmin)
admin.site.register(Paciente_documento,Paciente_documentoAdmin)
admin.site.register(App_documento,App_documentoAdmin)
admin.site.register(Vocalizacion,VocalizacionAdmin)
admin.site.register(App_enfermera_neurologo,App_enfermera_neurologoAdmin)
admin.site.register(App_enfermera_paciente,App_enfermera_pacienteAdmin)
admin.site.register(App_tipo_terapia,App_tipo_terapiaAdmin)
admin.site.register(Terapia,TerapiaAdmin)
admin.site.register(Recordatorio_terapia,Recordatorio_terapiaAdmin)
admin.site.register(Audio,AudioAdmin)
admin.site.register(Profesional_salud,Profesional_saludAdmin)
admin.site.register(Profesional_paciente,Profesional_pacienteAdmin)



