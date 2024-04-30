from django.shortcuts import render, redirect
from .forms import PostForm

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
