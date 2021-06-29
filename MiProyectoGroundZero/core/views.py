from core.forms import ContactoForm, RegistroForm, ProductoForm
from core.models import Usuario
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')
#
def index_user(request):
    return render(request,'core/index_user.html')

def Formulario_Publicacion(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Publicación realizada"
            
    return render(request,'core/Formulario_Publicacion.html',data)

def Formulario_Contacto(request):
    datos = {
        'form' : ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Gracias por Contactarnos. Recibiras una respuesta en menos de 24/hrs'

    return render(request,'core/Formulario_Contacto.html',datos)
#
def Formulario_Contacto_User(request):
    datos = {
        'form' : ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Gracias por Contactarnos. Recibiras una respuesta en menos de 24/hrs'

    return render(request,'core/Formulario_Contacto_User.html',datos)    

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

    #form = RegistroForm()

    datos = {
        'form' : RegistroForm
    }

    if request.method == 'POST':
        formulario = RegistroForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Registro Completado'

    return render(request,'core/Pagina_Registro.html',datos)

def Recuperar_Cuenta(request):
    return render(request,'core/Recuperar_Cuenta.html')

#Listar-agregar-eliminar-editar
def ListarUsuarios(request):
    usuarios = Usuario.objects.all()

    datos = {
        'usuarios' : usuarios
    }
    return render(request,'core/ListarUsuarios.html',datos)

def ListarProductos(request):
    return render(request,'core/ListarProductos.html')
