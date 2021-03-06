# Generated by Django 3.2.3 on 2021-06-29 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210628_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombreObra', models.CharField(max_length=100, verbose_name='Nombre Obra')),
                ('nombreAutor', models.CharField(max_length=100, verbose_name='Nombre Autor')),
                ('rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut')),
                ('correoElectronico', models.CharField(max_length=50, verbose_name='Correo Electronico')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('texto', models.TextField(max_length=200, verbose_name='Descripción')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
