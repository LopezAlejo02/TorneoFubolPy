# Generated by Django 4.0 on 2023-08-01 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('pais', models.CharField(max_length=50, null=True, verbose_name='Pais')),
                ('estrellas', models.FloatField(null=True, verbose_name='Numero de estrellas')),
                ('escudo', models.ImageField(null=True, upload_to='img/', verbose_name='Imagen del escudo')),
            ],
        ),
    ]
