# Generated by Django 4.0 on 2023-08-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_remove_jugador_copas_jugador_copasamerica_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='equipo',
            table='equipos',
        ),
        migrations.AlterModelTable(
            name='jugador',
            table='jugadores',
        ),
    ]