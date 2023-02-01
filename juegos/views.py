from django.shortcuts import render
from django.shortcuts import render
from .forms import *
from .models import *
from app.models import *
# Create your views here.
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

def memorama(request):
    get_juegos = Juego.objects.get(descripcion="Juego de memoria")
    get_img = gallery.objects.filter(user_id = request.user.id)
    print(get_juegos.descripcion)
    data = {
        'form':Resultado_Form,
        'get_img':get_img,
    }
    
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

def sopaletras(request):
    if request.user.is_authenticated:
        data = {
            'Sopa': Sopa_letra.objects.all(),
            'Sopa': Sopa_letra.objects.filter(user=request.user)
            }
    else:
        data = {
            'Sopa': Sopa_letra.objects.all()
        }
    return render(request, 'app/sopaletras.html', data)