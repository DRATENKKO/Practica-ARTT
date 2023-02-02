from django.db import models
from tipologias.models import *
# Create your models here.

#INSTITUCION
class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=100)
    descripcion_institucion = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_institucion)

#PROFESIONAL SALUD
class Profesional_salud(models.Model):
    id_profesional_salud = models.AutoField(primary_key=True)
    rut_profesional_salud = models.CharField(max_length=100)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    user = models.ForeignKey(to="app.usuario", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_profesional_salud)

#PROFESIONAL PACIENTE
class Profesional_paciente(models.Model):
    id_profesional_paciente = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_profesional_salud = models.ForeignKey(Profesional_salud, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(to="paciente.paciente", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_profesional_paciente)

#APP ENFERMERA PACIENTE
class App_enfermera_paciente(models.Model):
    id_app_enfermera_paciente = models.AutoField(primary_key=True)
    username_enfermera = models.CharField(max_length=100)
    username_paciente = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_enfermera_paciente)

#TERAPISTA
class Enfermera(models.Model):
    id_enfermera = models.AutoField(primary_key=True)
    rut_enfermera = models.CharField(max_length=100)
    nombre_enfermera = models.CharField(max_length=100)
    apellido_enfermera = models.CharField(max_length=100)
    direccion_enfermera = models.CharField(max_length=100)
    correo_enfermera = models.CharField(max_length=100)
    telefono_enfermera = models.CharField(max_length=100)
    whatsapp_enfermera = models.CharField(max_length=100)
    telegram_enfermera = models.CharField(max_length=100)
    celular_enfermera = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_enfermera)

#APP ENFERMERA NEUROLOGO
class App_enfermera_neurologo(models.Model):
    id_app_enfermera_neurologo = models.AutoField(primary_key=True)
    username_enfermera = models.CharField(max_length=100)
    username_neurologo = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_enfermera_neurologo)