from django.contrib import admin
from .models import Usuario, Rol, Usuario_Rol, Publicacion, RespuestaPublicacion

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Usuario_Rol)
admin.site.register(Publicacion)
admin.site.register(RespuestaPublicacion)
