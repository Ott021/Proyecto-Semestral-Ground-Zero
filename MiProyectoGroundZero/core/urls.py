from django.urls import path
from django.urls import URLPattern
from .views import index, Formulario_Contacto, Vista_Producto, Vista_Canasta
from .views import index_user, Formulario_Publicacion,Formulario_Contacto_User, Vista_Producto_User, Vista_Canasta_User
from .views import Pagina_Inicio_Sesion, Pagina_Registro, Recuperar_Cuenta
from .views import ListarUsuarios,ListarProductos,EditarProducto,EliminarProducto,EliminarUsuario
urlpatterns = [
    path('', index, name="index"),
    path('contacto/', Formulario_Contacto, name="Formulario_Contacto"),
    path('producto/', Vista_Producto, name="Vista_Producto"),
    path('canasta/', Vista_Canasta, name="Vista_Canasta"),
    #User
    path('user/', index_user, name="index_user"),
    path('user/publicar', Formulario_Publicacion, name="Formulario_Publicacion"),
    path('user/contacto/', Formulario_Contacto_User, name="Formulario_Contacto_User"),
    path('user/producto/', Vista_Producto_User, name="Vista_Producto_User"),
    path('user/canasta/', Vista_Canasta_User, name="Vista_Canasta_User"),
    #Inicio Sesion
    path('inicio_sesion/', Pagina_Inicio_Sesion, name="Pagina_Inicio_Sesion"),
    path('registrar/', Pagina_Registro, name="Pagina_Registro"),
    path('recuperacion/', Recuperar_Cuenta, name="Recuperar_Cuenta"),
    #Listar-agregar-eliminar-editar
    path('user/listarUsuarios',ListarUsuarios, name="ListarUsuarios"),
    path('user/listarProductos',ListarProductos, name="ListarProductos"),
    path('user/editarProducto/<id>', EditarProducto, name="EditarProducto"),
    path('user/eliminarProducto/<id>', EliminarProducto, name="EliminarProducto"),
    path('user/eliminarUsuario/<id>', EliminarUsuario, name="EliminarUsuario")

]