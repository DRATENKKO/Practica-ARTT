from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#REGION
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_region)

#PROVINCIA
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_comuna)

#COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_comuna)


#TIPO DE JUEGO
class Tipo_juego(models.Model):
    id_tipo_juego = models.AutoField(primary_key=True)
    nombre_juego  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_tipo_juego)

#TIPO USUARIO
class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre_tipo_usuario = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_tipo_usuario)

#USUARIO
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    issuperuser = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    id_telegram = models.CharField(max_length=100)
    id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_usuario)

#PACIENTE
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=100)
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    direccion_paciente = models.CharField(max_length=100)
    correo_paciente = models.CharField(max_length=100)
    telefono_paciente = models.CharField(max_length=100)
    whatsapp_paciente = models.CharField(max_length=100)
    telegram_paciente = models.CharField(max_length=100)
    celular_paciente = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_enfermera)

#terapista
class Terapista(models.Model):
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

#JUEGO
class Juego(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_tipo_juego = models.ForeignKey(Tipo_juego, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.descripcion)
    
#JUEGO
class Resultado_juego(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    resultado_1 = models.CharField(max_length=100)
    resultado_2 = models.CharField(max_length=100)
    resultado_3 = models.CharField(max_length=100)
    resultado_4 = models.CharField(max_length=100, blank=True, null=True)
    resultado_5 = models.CharField(max_length=100, blank=True, null=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id_juego = models.ForeignKey(Juego, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.id_usuario)

class Memorice(models.Model):
    acierto = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=100)
    movimientos = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)


class Galeria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagenes = models.ImageField(upload_to='imagenes-user')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.usuario)

