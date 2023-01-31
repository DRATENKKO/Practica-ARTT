from __future__ import unicode_literals
from django.contrib.auth.models import  AbstractUser, UserManager
from django.db import models
from paciente.models import *
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
#INSTITUCION
class Institucion(models.Model):
    id_institucion = models.AutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=100)
    descripcion_institucion = models.CharField(max_length=100)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_institucion)
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
#FAMILIAR
class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    rut_familiar = models.CharField(max_length=100)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_familiar)
#TIPO_PARENTESCO
class Tipo_parentesco(models.Model):
    id_tipo_parentesco = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_tipo_parentesco) + " " + self.parentesco
#FAMILIAR_PACIENTE
class Familiar_paciente(models.Model):
    id_familiar_paciente = models.AutoField(primary_key=True)
    paciente = models.ManyToManyField(Usuario, related_name='Paciente')
    familiar = models.ManyToManyField(Usuario, related_name='Familiar')
    parentesco = models.ForeignKey(Tipo_parentesco, on_delete=models.CASCADE)

    def Paciente(self):
        return "\n".join([str(p.id) for p in self.paciente.all()]) + "\n" + " " .join([p.username for p in self.paciente.all()])

    def Familiar(self):
        return "\n".join([str(p.id) for p in self.familiar.all()]) + "\n" + " " .join([p.username for p in self.familiar.all()])
    
    def __str__(self):
        return str(self.id_familiar_paciente)
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
#APP ENFERMERA NEUROLOGO
class App_enfermera_neurologo(models.Model):
    id_app_enfermera_neurologo = models.AutoField(primary_key=True)
    username_enfermera = models.CharField(max_length=100)
    username_neurologo = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_enfermera_neurologo)
#APP ENFERMERA PACIENTE
class App_enfermera_paciente(models.Model):
    id_app_enfermera_paciente = models.AutoField(primary_key=True)
    username_enfermera = models.CharField(max_length=100)
    username_paciente = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.id_app_enfermera_paciente)
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
#PROFESIONAL SALUD
class Profesional_salud(models.Model):
    id_profesional_salud = models.AutoField(primary_key=True)
    rut_profesional_salud = models.CharField(max_length=100)
    id_institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_profesional_salud)
#PROFESIONAL PACIENTE
class Profesional_paciente(models.Model):
    id_profesional_paciente = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_profesional_salud = models.ForeignKey(Profesional_salud, on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_profesional_paciente)
#TERAPISTA
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
#TRIVIA
class Trivia(models.Model):
    id_trivia = models.AutoField(primary_key=True)
    ordinal = models.CharField(max_length=100)
    pregunta_trivia = models.CharField(max_length=100)
    respuesta_trivia = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_trivia)
#SOPALETRAS
class Sopa_letras(models.Model):
    id_sopa = models.AutoField(primary_key=True)
    pregunta_sopa = models.CharField(max_length=100)
    word = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_sopa)