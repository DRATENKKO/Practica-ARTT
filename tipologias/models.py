from django.db import models
# Create your models here.
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
