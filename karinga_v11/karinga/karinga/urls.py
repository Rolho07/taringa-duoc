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
from core import views
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inicio', views.inicio, name='inicio'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar-sesion/', views.inicioSesion, name='iniciar-sesion'),
    path('cerrar-sesion/', views.cerrarSesion, name='cerrar-sesion'),
    path('post-genshin-impact-1/', views.postGenshin1, name='post-genshin'),
    path('post-hollow-knight-1/', views.postHollow1, name='post-hollow'),
    path('post-honkai-impact-1/', views.postHonkai1, name='post-honkai'),
    path('terminos-y-condiciones/', views.termycond, name='terminos-y-condiciones'),
    path('crear-post/', views.create_post, name='crear_post'),
]
