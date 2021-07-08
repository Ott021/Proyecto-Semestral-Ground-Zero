from rest_framework import fields, serializers
from core.models import Producto, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'