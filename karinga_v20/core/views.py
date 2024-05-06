from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from .models import Publicacion
from .forms import PublicacionForm
import re

def inicio(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'inicio.html', {'publicaciones': publicaciones})

def configuracion(request):
    return render(request, 'configuracion.html')

def registrarse(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Longitud de contraseña
        if not 6 <= len(password) <= 8:
            messages.error(request, 'La contraseña debe tener entre 6 y 8 caracteres')
            return redirect('registrarse')
        # Caracteres especiales
        if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password):
            messages.error(request, 'La contraseña debe tener al menos un caracter especial')
            return redirect('registrarse')
        # Números
        if not re.search(r"\d", password):
            messages.error(request, 'La contraseña debe tener al menos un número')
            return redirect('registrarse')
        # Mayúsculas
        if not re.search(r"[A-Z]", password):
            messages.error(request, 'La contraseña debe tener al menos una mayúscula')
            return redirect('registrarse')
        # Contraseñas iguales
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registrarse')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado')
            return redirect('registrarse')
        
        user = Usuario.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Usuario registrado correctamente')
        return redirect('iniciar-sesion')
    else:
        return render(request, 'registrar.html')

def inicio_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def post_genshin_1(request):
    return render(request, 'postGenshin1.html')

def post_hollow_1(request):
    return render(request, 'postHollowKnight1.html')

def post_honkai_1(request):
    return render(request, 'postHonkai1.html')

def termycond(request):
    return render(request, 'terycond.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect('inicio')
    else:
        form = PublicacionForm()
    return render(request, 'crear_post.html', {'form': form})

def listar_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'listar_publicaciones.html', {'publicaciones': publicaciones})