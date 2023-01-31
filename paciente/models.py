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