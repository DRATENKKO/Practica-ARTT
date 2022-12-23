from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#TIPO DE JUEGO
class Tipo_juego(models.Model):
    id_tipo_juego = models.AutoField(primary_key=True)
    nombre_juego  = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id_tipo_juego)

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

