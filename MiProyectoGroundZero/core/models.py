from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, verbose_name='Rut')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    email = models.CharField(max_length=50,verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Password')

    def __str__(self):
        return self.rut

