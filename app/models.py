from __future__ import unicode_literals
from django.contrib.auth.models import  AbstractUser, UserManager
from django.db import models
from paciente.models import *
from medico_y_enfermera.models import *
from juegos.models import *
from tipologias.models import *
#REGION
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nombre_region)
#PROVINCIA
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre_provincia)
#COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_comuna = models.CharField(max_length=100)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nombre_comuna)
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
        return str(self.nombre_tipo_usuario)
#USUARIOMANAGER
class UsuarioManager(UserManager):
    def create_user(self, username, nombre, apellido, correo, password = None):
        usuario = self.model(
            username    = username,
            first_name  = nombre,
            last_name   = apellido,
            email       = correo
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, nombre, apellido, correo, password):
        usuario = self.create_user(
            username = username,
            first_name = nombre,
            last_name = apellido,
            email = correo
        ) 
        usuario.usuario_administrador = True      
        usuario.save()
        return usuario 
#USUARIO
class Usuario(AbstractUser):
    id_telegram = models.CharField(max_length=100, null=True, default='@')
    Tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete= models.CASCADE, null=True)
    telefono = models.CharField(max_length=100, null=True, default='+569')
    direccion = models.CharField(max_length=100, null=True,)
    id_comuna = models.ForeignKey(Comuna, on_delete= models.CASCADE, null=True)

    def nombre_area(self):
        return "{}, {}, {}". format(str(self.id), self.username, self.Tipo_usuario)

    def __str__(self):
        return self.nombre_area()

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
#APP DOCUMENTO
class App_documento(models.Model):
    id_app_documento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    qr = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_documento)
#VOCALIZACION
class Vocalizacion(models.Model):
    id_vocalizacion = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    url_archivo_vocalizacion = models.CharField(max_length=100)
    duracion = models.CharField(max_length=100)
    bpminute = models.CharField(max_length=100)
    bpmeasure = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_vocalizacion)
#AUDIO
class Audio(models.Model):
    id_audio = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    url_archivo_audio = models.CharField(max_length=100)
    jitter_ppq5 = models.CharField(max_length=100)
    jitter_rap = models.CharField(max_length=100)
    maximum_pitch = models.CharField(max_length=100)
    error_jitter_ppq5 = models.CharField(max_length=100)
    error_jitter_rap = models.CharField(max_length=100)
    error_maximum_pitch = models.CharField(max_length=100)
    jitter_ppq5_IA = models.CharField(max_length=100)
    jitter_rap_IA = models.CharField(max_length=100)
    maximum_pitch_IA = models.CharField(max_length=100)
    error_jitter_ppq5_IA = models.CharField(max_length=100)
    error_jitter_rap_IA = models.CharField(max_length=100)
    error_maximum_pitch_IA = models.CharField(max_length=100)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_audio)
#RESULTADO JUEGO
class Resultado_juego(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    resultado_1 = models.CharField(max_length=100)
    resultado_2 = models.CharField(max_length=100)
    resultado_3 = models.CharField(max_length=100)
    resultado_4 = models.CharField(max_length=100, blank=True, null=True)
    resultado_5 = models.CharField(max_length=100, blank=True, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    timestampp = models.DateTimeField(auto_now_add=True)
    id_juego = models.ForeignKey(Juego, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.id_usuario)
#GALERIA
class gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='user-', null=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #cambiar nombre a etiqueta
    count_img = models.IntegerField(null=True, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)