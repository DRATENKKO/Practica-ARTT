from django.contrib import admin
from .models import *
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ["id_institucion", "nombre_institucion", "descripcion_institucion"]

class Profesional_saludAdmin(admin.ModelAdmin):
    list_display = ["id_profesional_salud", "rut_profesional_salud", "id_institucion", "user"]

class Profesional_pacienteAdmin(admin.ModelAdmin):
    list_display = ["id_profesional_paciente", "descripcion", "id_profesional_salud","id_paciente"]

class App_enfermera_pacienteAdmin(admin.ModelAdmin):
    list_display = ["id_app_enfermera_paciente", "username_enfermera", "username_paciente"]

class EnfermeraAdmin(admin.ModelAdmin):
    list_display = ["id_enfermera", "rut_enfermera", "nombre_enfermera", "apellido_enfermera", "direccion_enfermera", "correo_enfermera", "telefono_enfermera","whatsapp_enfermera","telegram_enfermera","celular_enfermera"]

class App_enfermera_neurologoAdmin(admin.ModelAdmin):
    list_display = ["id_app_enfermera_neurologo", "username_enfermera", "username_neurologo"]

#INSTITUCION
admin.site.register(Institucion,InstitucionAdmin)
#PROFESIONAL SALUD
admin.site.register(Profesional_salud,Profesional_saludAdmin)
#PROFESIONAL PACIENTE
admin.site.register(Profesional_paciente,Profesional_pacienteAdmin)
#APP ENFERMERA PACIENTE
admin.site.register(App_enfermera_paciente,App_enfermera_pacienteAdmin)
#ENFERMERA
admin.site.register(Enfermera,EnfermeraAdmin)
#APP ENFERMERA NEUROLOGO
admin.site.register(App_enfermera_neurologo,App_enfermera_neurologoAdmin)