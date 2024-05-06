from django.contrib import admin
from .models import Usuario, Rol, Usuario_Rol

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Usuario_Rol)
