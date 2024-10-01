from .models import *
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields=['nombre','apellido','edad'] # "__all__"

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Personas
        fields= "__all__"