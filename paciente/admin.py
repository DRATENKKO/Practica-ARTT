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

class App_tipo_terapiaAdmin(admin.ModelAdmin):
    list_display = ["id_app_tipo_terapia", "descripcion"]

class TerapiaAdmin(admin.ModelAdmin):
    list_display = ["id_terapia", "horarios","fonoaudiologo_id","paciente_id","id_app_tipo_terapia"]

class Recordatorio_terapiaAdmin(admin.ModelAdmin):
    list_display = ["id_recordatorio_terapia", "hora_recordatorio","receta_id","id_terapia"]

class IntensidadAdmin(admin.ModelAdmin):
    list_display = ["id_intensidad", "timestamp","url_archivo_intensidad","intensidad","mindb","maxdb","comentario","Paciente"]

class FamiliarAdmin(admin.ModelAdmin):
    list_display = ["id_familiar", "rut_familiar", "user"]

class Tipo_parentescoAdmin(admin.ModelAdmin):
    list_display = ["id_tipo_parentesco", "parentesco"]

class Familiar_pacienteAdmin(admin.ModelAdmin):
    list_display = ["Paciente","Familiar","parentesco"]

admin.site.register(Hipertension,HipertensionAdmin)
admin.site.register(Diabetes,DiabetesAdmin)
admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Paciente_documento,Paciente_documentoAdmin)
admin.site.register(App_tipo_terapia,App_tipo_terapiaAdmin)
admin.site.register(Terapia,TerapiaAdmin)
admin.site.register(Recordatorio_terapia,Recordatorio_terapiaAdmin)
admin.site.register(Intensidad,IntensidadAdmin)
admin.site.register(Familiar,FamiliarAdmin)
admin.site.register(Tipo_parentesco,Tipo_parentescoAdmin)
admin.site.register(Familiar_paciente,Familiar_pacienteAdmin)