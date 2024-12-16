# Importamos las clases necesarias desde el framework de Django REST y otros módulos
from rest_framework import serializers  # Importamos la clase base serializers
from .models import Anime  # Importamos el modelo Anime desde el archivo models.py
from django.contrib.auth.models import User  # Importamos el modelo User de Django para crear usuarios

class AnimeSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Anime, que se encarga de convertir los datos 
    del modelo Anime en formato JSON y viceversa.
    """
    class Meta:
        model = Anime  # Definimos el modelo con el que trabajará el serializador
        fields = '__all__'  # Incluye todos los campos del modelo Anime


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User, que se encarga de convertir los datos 
    del modelo User en formato JSON y viceversa.
    """
    # Establecemos que el campo 'password' solo se puede escribir, no leer
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Definimos el modelo con el que trabajará el serializador
        fields = ['username', 'password', 'email']  # Especificamos los campos a incluir en la serialización
        extra_kwargs = {'password': {'write_only': True}}  # Configuramos para que 'password' solo sea escribible

    def create(self, validated_data):
        """
        Sobrescribimos el método 'create' para asegurarnos de que al crear un nuevo usuario,
        la contraseña se maneje de manera segura usando el método 'create_user' de Django.
        """
        # Creamos el usuario con la contraseña correctamente cifrada
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # Si no se proporciona un email, se asigna un valor vacío
            password=validated_data['password']  # Usamos 'create_user' para cifrar la contraseña
        )
        return user  # Retornamos el usuario creado
