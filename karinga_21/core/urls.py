from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('configuracion/', views.configuracion, name='configuracion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('iniciar-sesion/', views.inicio_sesion, name='iniciar-sesion'),
    path('cerrar-sesion/', views.cerrarSesion, name='cerrar-sesion'),
    path('terminos-y-condiciones/', views.termycond, name='terminos-y-condiciones'),
    path('crear-post/', views.create_post, name='crear_post'),
    path('listar_publicaciones/', views.listar_publicaciones, name='listar_publicaciones'),
    path('detalle-publicacion/<int:publicacion_id>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('responder-publicacion/<int:publicacion_id>/', views.responder_publicacion, name='responder_publicacion'),
    #reset password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="confirmacion-email.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('free-games-api', views.free_games_api, name='free-games-api'),
    path('free-games-browser-api', views.free_games_browser_api, name='free-games-browser-api'),
    path('lista-post/', views.lista_post, name='lista-post'),  
    path('respuesta-post/', views.respuesta_post, name='respuesta-post'),
    path('votos-post/', views.votos_post, name='votos-post'), 
]