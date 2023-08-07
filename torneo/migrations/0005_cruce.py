# Generated by Django 4.0 on 2023-08-06 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_alter_equipo_table_alter_jugador_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruce',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.equipo')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.jugador')),
            ],
            options={
                'db_table': 'cruces',
            },
        ),
    ]
