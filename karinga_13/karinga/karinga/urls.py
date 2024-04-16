"""
URL configuration for karinga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from posts import views as posts_views
from django.urls import path, include
from .views import inicio
from .views import guardar_perfil


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.inicio, name='inicio'),
    path('inicio', core_views.inicio, name='inicio'),
    path('configuracion/', core_views.configuracion, name='configuracion'),
    path('registrarse/', core_views.registrarse, name='registrarse'),
    path('iniciar-sesion/', core_views.inicioSesion, name='iniciar-sesion'),
    path('cerrar-sesion/', core_views.cerrarSesion, name='cerrar-sesion'),
    path('post-genshin-impact-1/', core_views.postGenshin1, name='post-genshin'),
    path('post-hollow-knight-1/', core_views.postHollow1, name='post-hollow'),
    path('post-honkai-impact-1/', core_views.postHonkai1, name='post-honkai'),
    path('terminos-y-condiciones/', core_views.termycond, name='terminos-y-condiciones'),
    path('crear-post/', posts_views.create_post, name='crear_post'),
    path('guardar_perfil/', guardar_perfil, name='guardar_perfil'),
    path('', include('ccore.urls')),
]


