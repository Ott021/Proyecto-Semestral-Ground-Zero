from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Contacto, Usuario, Producto

class RegistroForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut','nombre','email','password']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['rut','nombreCompleto','correoElectronico','region','ciudad','texto']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'