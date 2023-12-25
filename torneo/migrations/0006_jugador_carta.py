# Generated by Django 5.0 on 2023-12-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("torneo", "0005_cruce"),
    ]

    operations = [
        migrations.AddField(
            model_name="jugador",
            name="carta",
            field=models.ImageField(
                null=True,
                upload_to="img/cartas",
                verbose_name="imagen de fondo de la carta del jugador",
            ),
        ),
    ]
