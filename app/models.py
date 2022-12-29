from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# get current u

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
        return str(self.nombre_tipo_usuario)

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, nombres, apellidos, id_telegram, id_tipo_usuario, password=None):
        if not email:
            raise ValueError('Los usuarios deben tener un correo electrónico')
        usuario = self.model(
            username = username,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos,
            id_telegram = id_telegram,
            id_tipo_usuario = id_tipo_usuario,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    def create_superuser(self, username, email, nombres, apellidos, id_telegram, id_tipo_usuario, password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            id_telegram = id_telegram,
            id_tipo_usuario = id_tipo_usuario,
            password = password,
        )
        usuario.usuario_administrador = True
        usuario.save(using=self._db)
        return usuario
#USUARIO
class Usuario(AbstractBaseUser):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario',unique=True,max_length=100)
    nombres = models.CharField('Nombres',max_length=100)
    apellidos = models.CharField('Apellidos',max_length=100)
    email = models.CharField('Correo electronico',max_length=100)
    id_telegram = models.CharField('Usuario Telegram',max_length=100)
    id_tipo_usuario = models.ForeignKey(Tipo_usuario,default=1 , on_delete=models.CASCADE)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres','apellidos','email','id_telegram']
    
    objects = UsuarioManager()
    def __str__(self):
        return f'{self.username},{self.apellidos}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

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
    
#JUEGO
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