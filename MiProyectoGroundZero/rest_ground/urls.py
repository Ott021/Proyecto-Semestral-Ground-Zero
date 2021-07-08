from django.urls import path
from rest_ground.views import detalle_usuario, lista_obras, lista_usuarios


urlpatterns = [
    path('usuarios',lista_usuarios,name="lista_usuarios"),
    path('usuarios/<id>',detalle_usuario,name="detalle_usuario"),
    path('obras',lista_obras,name="lista_obras")
]