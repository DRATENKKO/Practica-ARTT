from django.contrib import admin
from .models import *
# Register your models here.

class HipertensionAdmin(admin.ModelAdmin):
    list_display = ["id_hipertension", "estado_hipertension"]

class DiabetesAdmin(admin.ModelAdmin):
    list_display = ["id_diabetes", "tipo_diabetes"]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ["id_paciente", "rut_paciente", "telegram_paciente", "diabetes_id", "hipertension", "user", "paciente_familiar","whatsapp_paciente","celular_paciente"]

class Paciente_documentoAdmin(admin.ModelAdmin):
    list_display = ["id_paciente_documento", "autorizado", "timestamp","documento_id","id_paciente"]

admin.site.register(Hipertension,HipertensionAdmin)
admin.site.register(Diabetes,DiabetesAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Paciente_documento,Paciente_documentoAdmin)