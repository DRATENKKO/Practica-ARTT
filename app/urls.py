from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('memorama/', memorama, name="memorama"),
    path('subir_imagenes/', subir_imagenes, name="subir_imagenes"),
    path('crucigrama/', crucigrama, name="crucigrama"),
    path('grilla6x6/', grilla6x6, name="grilla6x6"),
    path('grilla8x8a/', grilla8x8, name="grilla8x8"),
    path('Juegos/',JuegosView.as_view(), name="JuegosView_list"),
    path('Juegos/<int:id>',JuegosView.as_view(), name="JuegosView_process"),
    path('registro/', registro, name="registro"),
]
