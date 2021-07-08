from django.urls import path
from rest_ground.views import lista_usuarios


urlpatterns = [
    path('usuarios',lista_usuarios,name="lista_usuarios")
]