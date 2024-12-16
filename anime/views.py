# Importamos las clases necesarias desde el framework de Django REST y otros módulos
from rest_framework import viewsets
from .models import Anime  # Importamos el modelo Anime que se encuentra en el archivo models.py
from .serializers import AnimeSerializer  # Importamos el serializador para el modelo Anime

from rest_framework import generics  # Importamos las vistas basadas en clases (generics)
from .serializers import UserSerializer  # Importamos el serializador para el modelo User
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django

# Definimos una vista basada en ViewSet para gestionar el modelo Anime
class AnimeViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona las operaciones CRUD estándar (listar, crear, actualizar, eliminar) 
    para el modelo Anime utilizando el serializador AnimeSerializer.
    """
   
    queryset = Anime.objects.all()  # Obtiene todos los objetos Anime de la base de datos
   
    serializer_class = AnimeSerializer

# Definimos una vista basada en generics.CreateAPIView para registrar nuevos usuarios
class UserRegisterView(generics.CreateAPIView):
    """
    Vista para registrar un nuevo usuario. Utiliza el serializador UserSerializer 
    para crear un nuevo usuario en la base de datos.
    """
    queryset = User.objects.all()  # Obtiene todos los usuarios de la base de datos
    serializer_class = UserSerializer  
