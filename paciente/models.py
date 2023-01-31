from django.db import models
from django.db import models
# Create your models here.
#HIPERTENSION
class Hipertension(models.Model):
    id_hipertension = models.AutoField(primary_key=True)
    estado_hipertension = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_hipertension)
#DIABETES
class Diabetes(models.Model):
    id_diabetes = models.AutoField(primary_key=True)
    tipo_diabetes = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_diabetes)
#USUARIO
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=100)
    telegram_paciente = models.CharField(max_length=100)
    diabetes_id = models.CharField(max_length=100)
    hipertension = models.CharField(max_length=100)
    user = models.ForeignKey(to="app.usuario", on_delete=models.CASCADE)
    paciente_familiar = models.CharField(max_length=100)
    whatsapp_paciente = models.CharField(max_length=100)
    celular_paciente = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_enfermera)
#PACIENTE_DOCUMENTO
class Paciente_documento(models.Model):
    id_paciente_documento = models.AutoField(primary_key=True)
    autorizado = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    documento_id = models.CharField(max_length=100)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_paciente_documento)
#APP TIPO TERAPIA
class App_tipo_terapia(models.Model):
    id_app_tipo_terapia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_tipo_terapia)
#TERAPIA
class Terapia(models.Model):
    id_terapia = models.AutoField(primary_key=True)
    horarios = models.CharField(max_length=100)
    fonoaudiologo_id = models.CharField(max_length=100)
    paciente_id = models.CharField(max_length=100)
    id_app_tipo_terapia = models.ForeignKey(App_tipo_terapia, on_delete=models.CASCADE)
    #  ??? id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_terapia)

#RECORDATORIO TERAPIA
class Recordatorio_terapia(models.Model):
    id_recordatorio_terapia = models.AutoField(primary_key=True)
    hora_recordatorio = models.CharField(max_length=100)
    receta_id = models.CharField(max_length=100)
    id_terapia = models.ForeignKey(Terapia, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_recordatorio_terapia)

#INTENSIDAD
class Intensidad(models.Model):
    id_intensidad = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    url_archivo_intensidad = models.CharField(max_length=100)
    intensidad = models.CharField(max_length=100)
    mindb = models.CharField(max_length=100)
    maxdb = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_intensidad)