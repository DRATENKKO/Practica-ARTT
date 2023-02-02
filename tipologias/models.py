from django.db import models

# Create your models here.
#REGION
class Regiones(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_region = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.nombre_region)

# #PROVINCIA
# class Provincia(models.Model):
#     id_provincia = models.AutoField(primary_key=True)
#     nombre_provincia = models.CharField(max_length=100)
#     id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return str(self.nombre_provincia)
