from rest_framework import serializers
from core.models import Publicacion, RespuestaPublicacion, Votos

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'

class RespuestaPublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaPublicacion
        fields = '__all__'

class VotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votos
        fields = '__all__'