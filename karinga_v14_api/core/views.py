from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import re

#API REST
from rest_framework import generics
from .models import Post, PostReply, UsuarioPersonalizado
from .serializers import PostSerializer, PostReplySerializer, UsuarioPersonalizadoSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostReplyList(generics.ListCreateAPIView):
    queryset = PostReply.objects.all()
    serializer_class = PostReplySerializer

class PostReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostReply.objects.all()
    serializer_class = PostReplySerializer

class UsuarioPersonalizadoList(generics.ListCreateAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioPersonalizadoSerializer

class UsuarioPersonalizadoDetail(generics.RetrieveAPIView):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioPersonalizadoSerializer

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

@login_required
def guardar_perfil(request):
    if request.method == 'POST':
        # Obtener o crear el objeto UsuarioPersonalizado asociado al usuario actual
        usuario_personalizado, creado = UsuarioPersonalizado.objects.get_or_create(user=request.user)
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        # Actualizar el perfil del usuario personalizado
        usuario_personalizado.nombre = nombre
        usuario_personalizado.apellido = apellido
        usuario_personalizado.save()
        return redirect('perfil')  # Redireccionar a la página de perfil
    else:
        # Si la solicitud no es POST, probablemente sea un error, manejarlo aquí
        pass