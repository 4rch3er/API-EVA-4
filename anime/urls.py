from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importamos las vistas que hemos definido para manejar las solicitudes
from .views import AnimeViewSet
from .views import UserRegisterView

router = DefaultRouter()
router.register(r'animes', AnimeViewSet)

# Definimos las URLs del proyecto
urlpatterns = [
    path('', include(router.urls)),# El 'router.urls' se encarga de definir todas las rutas necesarias para las operaciones CRUD (GET, POST, PUT, DELETE)    
    path('register/', UserRegisterView.as_view(), name='register'),# La vista 'UserRegisterView' se encargará de gestionar las solicitudes para crear un nuevo usuario
]