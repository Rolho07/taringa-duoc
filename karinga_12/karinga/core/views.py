from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def configuracion(request):
    return render(request, 'configuracion.html')

def registrarse(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registrarse')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return redirect('registrarse')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuario registrado correctamente')
        return redirect('iniciar-sesion')
    else:
        return render(request, 'registrar.html')

def inicioSesion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión correcto')
            return redirect('inicio')
        else:
            messages.error(request, 'Email o contraseña incorrectos')
            return redirect('iniciar-sesion')
        
    return render(request, 'inicio sesion.html')

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

@login_required
def postGenshin1(request):
    return render(request, 'postGenshin1.html')

@login_required
def postHollow1(request):
    return render(request, 'postHollowKnight1.html')

@login_required
def postHonkai1(request):
    return render(request, 'postHonkai1.html')

def termycond(request):
    return render(request, 'terycond.html')