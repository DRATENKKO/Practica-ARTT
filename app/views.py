from django.shortcuts import render
from .forms import *
from .models import *
# importar api
from rest_framework import viewsets
import os
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
import json
from django.contrib.auth import get_user
from django.contrib.auth.models import User

# CREACION DE VISTAS

@csrf_exempt
@api_view(['GET', 'POST'])
def api(request):
    if request.method == 'GET':
        names = []
        for path in os.listdir('imagenes-user/user-'):
            names.append(path)
        pass
    elif request.method == 'POST':
        # Código para manejar la solicitud POST
        pass
    return JsonResponse({'names': names})

def grilla6x6(request):
    data = {
        'form':Resultado_Form,
    }
    if request.method == 'POST':
        print("ESTOY ADENTRO DEL IFFF")
        formulario = Resultado_Form(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.resultado_1 = request.POST["resultado_1"]
            post.resultado_2 = request.POST["resultado_2"]
            post.resultado_3 = request.POST["resultado_3"]
            post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = Resultado_Form()
    return render(request, 'app/grilla6x6.html', data)


def grilla8x8(request):
    data = {
        'form': MemoriceForm,
    }
    if request.method == 'POST':
        print("ESTOY ADENTRO DEL IFFF")
        formulario = MemoriceForm(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.acierto = request.POST["acierto"]
            post.tiempo = request.POST["tiempo"]
            post.movimientos = request.POST["movimientos"]
            post.usuario_id = request.user.id
            formulario.save()
        else:
            formulario = MemoriceForm()
    return render(request, 'app/grilla8x8.html')

    # return render(request, 'app/subir_imagenes.html')


def crucigrama(request):
    return render(request, 'app/crucigrama.html')


def index(request):
    return render(request, 'app/index.html')



def registro(request):
    data = {
        'form': CustomUserCreationForm,
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, User)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        else:
            formulario = CustomUserCreationForm()
    
    return render(request, 'registration/registro.html', data)
###################### MEMORICE #######################
################ NO TOCAR DE MOMENTO ##################


def memorama(request):
    get_juegos = Juego.objects.get(descripcion="Juego de memoria")
    print(get_juegos.descripcion)
    data = {
        'form':Resultado_Form,
    }
    print(request.user.id)
    if request.method == 'POST':
        formulario = Resultado_Form(data=request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.resultado_1 = request.POST["Resultado_1"]
            post.resultado_2 = request.POST["Resultado_2"]
            post.resultado_3 = request.POST["Resultado_3"]
            post.id_usuario_id = request.user.id
            post.id_juego_id = get_juegos.id
            post.save()
            formulario.save()
        else:
            formulario = Resultado_Form()
    return render(request, 'app/memorama.html', data)


def subir_imagenes(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        user = User.objects.get(username=request.user.username)

        for image in images:
            gallery.objects.create(image = image, user = user)

        uploaded_images = gallery.objects.all()
        return JsonResponse({"images": [{"url": image.image.url} for image in uploaded_images]})
    return render(request, "app/subir_imagenes.html")

class JuegosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):

#si la id es mayor a 0, se busca el juego con esa id

        if (id > 0):
            Juegos = list(Resultado_juego.objects.filter(id_resultado=id).values())
            if len(Juegos) > 0:
                Juego=Juegos[0]
                datos = {'message': 'Juegos encontrados', 'Juegos': Juegos[0]}
            else:
                datos = {'message': 'No se encontraron Juegos'}
            return JsonResponse(datos)

#se buscan todos los juegos

        Juegos = list(Resultado_juego.objects.values())
        if len(Juegos) > 0:
            datos = {'message': 'Juegos encontrados', 'Juegos': Juegos}
        else:
            datos = {'message': 'No se encontraron Juegos'}
        
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        
# se hace la insercion de los datos
        data = {
        'form': Resultado_juegoForm(),
        }
        Resultado_juego.objects.create(resultado_1=jd['resultado_1'], resultado_2=jd['resultado_2'], resultado_3=jd['resultado_3'])
        datos = {'message': 'Juegos encontrados'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        Juegos = list(Resultado_juego.objects.filter(id_resultado=id).values())
        if len(Juegos) > 0:
            Juego = Resultado_juego.objects.get(id_resultado=id)
            Juego.resultado_1 = jd['resultado_1']
            Juego.resultado_2 = jd['resultado_2']
            Juego.resultado_3 = jd['resultado_3']
            Juego.save()
            datos = {'message': 'Juegos actualizados'}
        else:
            datos = {'message': 'No se encontraron Juegos'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        Juegos = list(Resultado_juego.objects.filter(id_resultado=id).values())
        if len(Juegos) > 0:
            Juego = Resultado_juego.objects.get(id_resultado=id)
            Juego.delete()
            datos = {'message': 'Juegos eliminados'}
        else:
            datos = {'message': 'No se encontraron Juegos'}
        return JsonResponse(datos)

    # return render(request, 'app/memorama.html')


