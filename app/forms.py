from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm , ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.crypto import get_random_string


# class Resultado_Form(forms.ModelForm):

    
#     Resultado_1 = forms.CharField(label='Cantidad de aciertos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de aciertos',
#             'id': 'total_acierto'
#         }))

#     Resultado_2 = forms.CharField(label='Cantidad de tiempo', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de tiempo',
#             'id': 'total_tiempo'
#         }))

#     Resultado_3 = forms.CharField(label='Cantidad de movimientos', widget=forms.TextInput(
#         attrs={

#             'placeholder': 'Ingresa cantidad de movimientos',
#             'id': 'total_movimientos'
#         }))

#     class Meta:
#         model = Resultado_juego
#         fields = 'Resultado_1', 'Resultado_2', 'Resultado_3'

class CustomUserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email' )
    def clean_password(self):
        return self.initial["password"]

class CustomUserCreationForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    username = forms.CharField(label='Usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'username'
        }))

    first_name = forms.CharField(label='Nombres', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese sus nombres',
            'id': 'first_name'
        }))

    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese sus apellidos',
            'id': 'last_name'
        }))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese su correo electronico',
        'id': 'email'
    }))

    id_telegram = forms.CharField(label='Telegram', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su telegram',
            'id': 'password'
        }))



    direccion = forms.CharField(label='direccion', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su direccion',
            'id': 'password'
        }))

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese Contraseña',
            'id': 'password'
        }))
    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'email', 'id_telegram','telefono','direccion', 'password'

    def clean_password(self):
        """ validacion de contraseña
        metodo que valida la contraseña 
        """
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        # guardar la informacion del registro en la variable user
        user = super().save(commit=False)
        # encriptar contraseña
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        

# Form usuario por consola

class FormaRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Usuario.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username ya registrado")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return password2

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
