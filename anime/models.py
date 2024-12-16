from django.db import models

#Modelo que representa un Anime en la base de datos.
#Incluye varios campos para almacenar información relevante sobre el anime

class Anime(models.Model):
    
    titulo = models.CharField(max_length=255)
    tipo_anime = models.CharField(max_length=100)
    episodios = models.IntegerField()
    url = models.URLField()
    fecha = models.DateField()
    estado = models.CharField(max_length=100)
    generos = models.CharField(max_length=255)
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo
