from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# MEMORICE

class Resultado_Form(forms.ModelForm):
    
    Resultado_1 = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de aciertos',
            'id': 'total_acierto'
        }))

    Resultado_2 = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de tiempo',
            'id': 'total_tiempo'
        }))

    Resultado_3 = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
        attrs={

            'placeholder': 'Ingresa cantidad de movimientos',
            'id': 'total_movimientos'
        }))

    class Meta:
        model = Resultado_juego
        fields = 'Resultado_1', 'Resultado_2', 'Resultado_3'
        
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
            'id': 'password1',
            'required': 'required'
        }))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
            'id': 'password2',
            'required': 'required'
        }))
    
    
    class Meta:
        model = Usuario
        #all fields
        fields = 'username','email','nombres','apellidos', 'id_telegram'

    username = models.CharField('Nombre de usuario',unique=True,max_length=100)
    nombres = models.CharField('Nombres',max_length=100)
    apellidos = models.CharField('Apellidos',max_length=100)
    email = models.CharField('Correo electronico',max_length=100)
    id_telegram = models.CharField('Usuario Telegram',max_length=100)


# ['username', 'password1','first_name', 'last_name','email','id_telegram',]

    # id_usuario = models.AutoField(primary_key=True)
    # #password = models.CharField(max_length=100)
    # #username = models.CharField(max_length=100)
    # #first_name = models.CharField(max_length=100)
    # #last_name = models.CharField(max_length=100)
    ## email = models.CharField(max_length=100)
    # #id_telegram = models.CharField(max_length=100)
    # id_tipo_usuario = models.ForeignKey(Tipo_usuario, on_delete=models.CASCADE)


# class MemoriceForm(forms.ModelForm):
#     acierto = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de aciertos',
#             'id': 'total_acierto'
#         }))

#     tiempo = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de tiempo',
#             'id': 'total_tiempo'
#         }))

#     movimientos = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de movimientos',
#             'id': 'total_movimientos'
#         }))

#     class Meta:
#         model = Memorice
#         fields = 'acierto', 'tiempo', 'movimientos'
