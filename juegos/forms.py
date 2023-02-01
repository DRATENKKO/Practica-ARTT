from django import forms
from .models import *

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