from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *

class UserAdmin(BaseUserAdmin):
    form = CustomUserCreationForm
    add_form = CustomUserCreationForm
    fieldsets = (
        ('User Profile', {'fields': ('username','Tipo_usuario', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion', 'password' )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','Tipo_usuario', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion', 'password'),
            
        }),
    )
    list_display = ('username','id','Tipo_usuario', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion', 'password')

class galleryAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "user","timestamp"]


class JuegoAdmin(admin.ModelAdmin):
    list_display = ["id", "descripcion"]

class RegionAdmin(admin.ModelAdmin):
    list_display = ["id_region", "nombre_region"]

class App_documentoAdmin(admin.ModelAdmin):
    list_display = ["id_app_documento", "titulo", "documento","descripcion","qr"]

class VocalizacionAdmin(admin.ModelAdmin):
    list_display = ["id_vocalizacion", "timestamp","url_archivo_vocalizacion","duracion","bpminute","bpmeasure","comentario","Paciente"]

class AudioAdmin(admin.ModelAdmin):
    list_display = ["id_audio", "timestamp","url_archivo_audio","jitter_ppq5","jitter_rap","maximum_pitch","error_jitter_ppq5","error_jitter_rap","error_maximum_pitch","jitter_ppq5_IA","jitter_rap_IA","maximum_pitch_IA","error_jitter_ppq5_IA","error_jitter_rap_IA","error_maximum_pitch_IA","id_paciente"]

#USUARIO
admin.site.register(Usuario,UserAdmin)
#GALLERY
admin.site.register(gallery,galleryAdmin)
#APP DOCUMENTO
admin.site.register(App_documento,App_documentoAdmin)
#VOCALIZACION
admin.site.register(Vocalizacion,VocalizacionAdmin)
#AUDIO
admin.site.register(Audio,AudioAdmin)