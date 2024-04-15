from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def configuracion(request):
    return render(request, 'configuracion.html')

def registrarse(request):
    return render(request, 'registrar.html')

def inicioSesion(request):
    return render(request, 'inicio sesion.html')

def postGenshin1(request):
    return render(request, 'postGenshin1.html')

def postHollow1(request):
    return render(request, 'postHollowKnight1.html')

def postHonkai1(request):
    return render(request, 'postHonkai1.html')

def termycond(request):
    return render(request, 'terycond.html')