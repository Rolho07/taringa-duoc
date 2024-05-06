from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    tipo_rol = models.CharField(max_length=30)

class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class Publicacion(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='karinga/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class RespuestaPublicacion(models.Model):
    contenido_respuesta = models.TextField()
    fecha_creacion_respuesta = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Usuario_Rol(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Votos(models.Model):
    tipo_votos = models.CharField(max_length=8)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
