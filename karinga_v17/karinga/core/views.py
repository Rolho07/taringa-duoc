from django.shortcuts import render, redirect
from django.contrib import messages
import re
from .models import Publicacion, RespuestaPublicacion, Usuario

# API REST
from rest_framework import generics
from .serializers import PublicacionSerializer, RespuestaPublicacionSerializer, UsuarioSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

class PostReplyList(generics.ListCreateAPIView):
    queryset = RespuestaPublicacion.objects.all()
    serializer_class = RespuestaPublicacionSerializer

class PostReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespuestaPublicacion.objects.all()
    serializer_class = RespuestaPublicacionSerializer

class UsuarioPersonalizadoList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioPersonalizadoDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Create your views here.
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
            # Aquí podrías realizar alguna acción adicional si lo deseas
            return redirect('inicio')
        else:
            messages.error(request, 'Email o contraseña incorrectos')
            return redirect('inicioSesion')
        
    return render(request, 'inicio sesion.html')

def cerrarSesion(request):
    logout(request)
    return redirect('inicio')

def postGenshin1(request):
    return render(request, 'postGenshin1.html')

def postHollow1(request):
    return render(request, 'postHollowKnight1.html')

def postHonkai1(request):
    return render(request, 'postHonkai1.html')

def termycond(request):
    return render(request, 'terycond.html')

def guardar_perfil(request):
    if request.method == 'POST':
        # Obtener o crear el objeto Usuario asociado al usuario actual
        usuario, creado = Usuario.objects.get_or_create(username=request.user)
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        # Actualizar el perfil del usuario
        usuario.nombres = nombre
        usuario.apellidos = apellido
        usuario.save()
        return redirect('perfil')  # Redireccionar a la página de perfil
    else:
        # Si la solicitud no es POST, probablemente sea un error, manejarlo aquí
        pass

def reset_password_request(request):
    if request.method == "POST":
        email = request.POST['email']
        associated_users = Usuario.objects.filter(email=email)
        if associated_users.exists():
            for user in associated_users:
                subject = "Restablecimiento de contraseña"
                email_template_name = "autenticacion/password_reset_email.txt"
                c = {
                    "email": user.email,
                    'domain': settings.SITE_URL,
                    'site_name': 'Su Sitio',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)), # type: ignore
                    "user": user,
                    'token': default_token_generator.make_token(user), # type: ignore
                    }
                email = render_to_string(email_template_name, c) # type: ignore
                try:
                    send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email], fail_silently=False) # type: ignore
                except BadHeaderError: # type: ignore
                    return HttpResponse('Invalid header found.') # type: ignore
                return redirect ("/password_reset/done/")
        return render(request=request, template_name="autenticacion/password_reset_form.html")
