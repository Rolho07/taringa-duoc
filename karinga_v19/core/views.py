from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Usuario
from .forms import PublicacionForm
import re

def inicio(request):
    return render(request, 'inicio.html')

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

def inicioSesion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            messages.success(request, 'Inicio de sesión correcto')
            return redirect('inicio')
        else:
            messages.error(request, 'Email o contraseña incorrectos')
            return redirect('inicioSesion')
        
    return render(request, 'inicio_sesion.html')

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

def create_post(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('inicio')
    else:
        form = PublicacionForm()
    return render(request, 'crear_post.html', {'form': form})