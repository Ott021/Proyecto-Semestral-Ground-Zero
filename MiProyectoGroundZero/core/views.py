from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')
#
def index_user(request):
    return render(request,'core/index_user.html')

def Formulario_Publicacion(request):
    return render(request,'core/Formulario_Publicacion.html')

def Formulario_Contacto(request):
    return render(request,'core/Formulario_Contacto.html')
#
def Formulario_Contacto_User(request):
    return render(request,'core/Formulario_Contacto_User.html')    

def Vista_Producto(request):
    return render(request,'core/Vista_Producto.html')
#
def Vista_Producto_User(request):
    return render(request,'core/Vista_Producto_User.html')

def Vista_Canasta(request):
    return render(request,'core/Vista_Canasta.html')
#
def Vista_Canasta_User(request):
    return render(request,'core/Vista_Canasta_User.html')

#Ingreso usuarios
def Pagina_Inicio_Sesion(request):
    return render(request,'core/Pagina_Inicio_Sesion.html')

def Pagina_Registro(request):
    return render(request,'core/Pagina_Registro.html')

def Recuperar_Cuenta(request):
    return render(request,'core/Recuperar_Cuenta.html')

