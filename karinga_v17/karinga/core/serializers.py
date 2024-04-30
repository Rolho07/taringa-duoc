from rest_framework import serializers
from .models import Publicacion, RespuestaPublicacion, Usuario

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class RespuestaPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPublicacion
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
