from django.contrib import admin
from .models import *
# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    list_display = ["id_region", "nombre_region"]

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ["id_provincia", "nombre_provincia", "id_region"]

# #REGION
# admin.site.register(Regiones,RegionAdmin)
# #PROVINCIA
# admin.site.register(Provincia,ProvinciaAdmin)