from django.shortcuts import render, redirect
from .forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UsuarioPersonalizado

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('inicio')  # Redirigir a la página de inicio después de crear el post
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

@login_required
def guardar_perfil(request):
    if request.method == 'POST':
        usuario = request.user
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        # Actualizar el perfil del usuario
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.save()
        return redirect('perfil')  # Redireccionar a la página de perfil
    else:
        pass