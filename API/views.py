from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import *

class UsuarioViewSet(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PersonaViewSet(generics.ListCreateAPIView):
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer
