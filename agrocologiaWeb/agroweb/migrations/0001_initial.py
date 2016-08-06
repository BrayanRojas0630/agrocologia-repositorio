# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_imagen', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='/imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_oferta', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('valor_descuento', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('fecha_vencimiento', models.DateField()),
                ('duracion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('propietario', models.CharField(max_length=100)),
                ('id_oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroweb.Ofertas')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rol', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('comprar', models.CharField(max_length=100)),
                ('vender', models.CharField(max_length=100)),
                ('solicitud', models.CharField(max_length=100)),
                ('contestar_solicitud', models.CharField(max_length=100)),
                ('cambiar_estado', models.CharField(max_length=100)),
                ('publicar_noticias', models.CharField(max_length=100)),
                ('consultar_historial', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipos_Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_question', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('documeto', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=100)),
                ('placa_carro', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('codigo_postal', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroweb.Roles')),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='id_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroweb.Tipos_Productos'),
        ),
        migrations.AddField(
            model_name='imagen_producto',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agroweb.Productos'),
        ),
    ]