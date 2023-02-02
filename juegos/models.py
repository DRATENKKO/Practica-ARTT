from django.db import models

# Create your models here.

#SOPALETRAS
class Sopa_letra(models.Model):
    id_sopa = models.AutoField(primary_key=True)
    pregunta_sopa = models.CharField(max_length=100)
    word = models.CharField(max_length=50)
    direction = models.CharField(max_length=50)
    start = models.CharField(max_length=50)
    user = models.ForeignKey(to="app.usuario", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_sopa)

#TRIVIA
class Trivia(models.Model):
    id_trivia = models.AutoField(primary_key=True)
    ordinal = models.CharField(max_length=100)
    pregunta_trivia = models.CharField(max_length=100)
    respuesta_trivia = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(to="app.usuario", on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id_trivia)

#JUEGO
class Juego(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    id_tipo_juego = models.ForeignKey(to="tipologias.tipo_juego", on_delete=models.CASCADE)

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
    id_usuario = models.ForeignKey(to="app.usuario", on_delete=models.CASCADE, null=True, blank=True)
    timestampp = models.DateTimeField(auto_now_add=True)
    id_juego = models.ForeignKey(Juego, on_delete=models.CASCADE , null=True)
    def __str__(self):
        return str(self.id_usuario)