from django.urls import path
from rest_ground.views import detalle_obra,detalle_usuario, lista_obras, lista_usuarios
from .viewslogin import login


urlpatterns = [
    path('usuarios',lista_usuarios,name="lista_usuarios"),
    path('usuarios/<id>',detalle_usuario,name="detalle_usuario"),
    path('obras',lista_obras,name="lista_obras"),
    path('obras/<id>',detalle_obra,name="detalle_obra"),
    path('login',login, name='login')
]