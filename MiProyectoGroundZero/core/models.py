from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    email = models.CharField(max_length=50,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Password')

    def __str__(self):
        return self.rut

class Contacto(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombreCompleto = models.CharField(max_length=100,verbose_name='NombreCompleto')
    correoElectronico = models.CharField(max_length=50,verbose_name='CorreoElectronico')
    region = models.CharField(max_length=30,verbose_name='Region')
    ciudad = models.CharField(max_length=30,verbose_name='Ciudad')
    texto = models.TextField(max_length=200,verbose_name='Texto')

    def __str__(self):
        return self.rut

class Producto (models.Model):
    nombreObra = models.CharField(max_length=100,verbose_name='Nombre Obra')
    nombreAutor = models.CharField(max_length=100,verbose_name='Nombre Autor')
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    correoElectronico = models.CharField(max_length=50,verbose_name='Correo Electronico')
    telefono = models.IntegerField(verbose_name='Telefono')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio = models.IntegerField(verbose_name='Precio')
    texto = models.TextField(max_length=200,verbose_name='Descripción')
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombreObra

