from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#CRUCIGRAMA
class TriviaForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Trivia
        fields = "__all__"


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



class CustomUserCreationForm(forms.ModelForm):

    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'username'
        }))

    first_name = forms.CharField(label=' ingrese su nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'first_name'
        }))

    last_name = forms.CharField(label=' ingrese su apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su nombre de usuario',
            'id': 'last_name'
        }))

    email = forms.EmailField(label='correo electronico', widget=forms.EmailInput(attrs={
        'class': 'form-control mb-2',
        'placeholder': 'Ingrese su correo electronico',
        'id': 'email'
    }))

    id_telegram = forms.CharField(label='telegram', widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Ingrese su telegram',
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
        fields = 'username', 'first_name', 'last_name', 'email', 'id_telegram', 'password'

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
