from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario, Publicacion, RespuestaPublicacion
from .forms import PublicacionForm, FormularioRespuesta
import re
#API
from .models import Publicacion, RespuestaPublicacion, Votos
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import PublicacionSerializer, RespuestaPublicacionSerializer, VotosSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_post(request):
    if request.method == 'GET':
        publicaciones = Publicacion.objects.all()
        serializer = PublicacionSerializer(publicaciones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HYYP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'POST'])
def respuesta_post(request):
    if request.method == 'GET':
        respuesta = RespuestaPublicacion.objects.all()
        serializer = RespuestaPublicacionSerializer(respuesta, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RespuestaPublicacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HYYP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@csrf_exempt
@api_view(['GET', 'POST'])
def votos_post(request):
    if request.method == 'GET':
        votos = Votos.objects.all()
        serializer = VotosSerializer(votos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VotosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HYYP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#API EXTERNA
def free_games_api(request):
    return render(request, 'freegamesapiPC.html')

def free_games_browser_api(request):
    return render(request, 'freegamesapiNAV.html')

        ##########################################################

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

def termycond(request):
    return render(request, 'terycond.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
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

def detalle_publicacion(request, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion})

def responder_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        formulario = FormularioRespuesta(request.POST)
        if formulario.is_valid():
            contenido_respuesta = formulario.cleaned_data['contenido']
            nueva_respuesta = RespuestaPublicacion(contenido_respuesta=contenido_respuesta, publicacion=publicacion, usuario=request.user)
            nueva_respuesta.save()  # Guardar la nueva respuesta en la base de datos
            return redirect('detalle_publicacion', publicacion_id=publicacion_id)
    else:
        formulario = FormularioRespuesta()
    return render(request, 'responder_publicacion.html', {'publicacion': publicacion, 'formulario': formulario})