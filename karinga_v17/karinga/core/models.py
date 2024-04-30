from django.contrib.auth.models import AbstractUser
from django.db import models

class Rol(models.Model):
    rol_id = models.AutoField(primary_key=True)
    tipo_rol = models.CharField(max_length=30)

class Usuario(AbstractUser):
    usuario_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Publicacion(models.Model):
    publicacion_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class RespuestaPublicacion(models.Model):
    respuesta_id = models.AutoField(primary_key=True)
    contenido_respuesta = models.TextField()
    fecha_creacion_respuesta = models.DateField()
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Usuario_Rol(models.Model):
    usuario_rol_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Votos(models.Model):
    votos_id = models.AutoField(primary_key=True)
    tipo_votos = models.CharField(max_length=8)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)