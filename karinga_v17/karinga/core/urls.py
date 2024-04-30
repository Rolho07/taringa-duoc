from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from core import views as core_views
from posts import views as posts_views
from core.views import guardar_perfil
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
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
    # API
    path('api/posts/', core_views.PostList.as_view(), name='post_list'),
    path('api/posts/<int:pk>/', core_views.PostDetail.as_view(), name='post_detail'),
    path('api/post-replies/', core_views.PostReplyList.as_view(), name='reply_list'),
    path('api/post-replies/<int:pk>/', core_views.PostReplyDetail.as_view(), name='reply_detail'),
    path('api/usuarios/', core_views.UsuarioPersonalizadoList.as_view(), name='usuario_list'),
    path('api/usuarios/<int:pk>/', core_views.UsuarioPersonalizadoDetail.as_view(), name='usuario_detail'),
    #reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]