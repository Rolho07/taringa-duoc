from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar-sesion/', views.inicioSesion, name='iniciar-sesion'),
    path('cerrar-sesion/', views.cerrarSesion, name='cerrar-sesion'),
    path('post-genshin-impact-1/', views.post_genshin_1, name='post-genshin'),
    path('post-hollow-knight-1/', views.post_hollow_1, name='post-hollow'),
    path('post-honkai-impact-1/', views.post_honkai_1, name='post-honkai'),
    path('terminos-y-condiciones/', views.termycond, name='terminos-y-condiciones'),
    path('crear-post/', views.create_post, name='crear_post'),
]