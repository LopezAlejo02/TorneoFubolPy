from django.db import models

# Create your models here.


class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    pais = models.CharField(max_length=25, null=True, verbose_name='Pais')
    estrellas = models.FloatField(
        null=True, verbose_name='Numero de estrellas')
    escudo = models.ImageField(
        upload_to='img/escudos', null=True, verbose_name='Imagen del escudo')

    class Meta:
        db_table = 'equipos'


class Jugador(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, verbose_name='Nombre')
    estrellas = models.IntegerField(
        null=True, verbose_name='Numero de estrellas')
    copasAmerica = models.IntegerField(
        null=True, verbose_name='Numero de copas America')
    copasEuro = models.IntegerField(
        null=True, verbose_name='Numero de copas de Europa')
    copasMundial = models.IntegerField(
        null=True, verbose_name='Numero de copas mundiales')
    foto = models.ImageField(upload_to='img/jugadores',
                             null=True, verbose_name='Foto del jugador')
    carta = models.ImageField(upload_to='img/cartas',
                             null=True, verbose_name='imagen de fondo de la carta del jugador')

    class Meta:
        db_table = 'jugadores'

class Cruce(models.Model):
    id = models.AutoField(primary_key=True)
    jugador = models.ForeignKey(Jugador, null=False, blank=False, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'cruces'

class Partido(models.Model):
    id = models.AutoField(primary_key=True)
    jugadorLocal = models.ForeignKey(Jugador, null=False, blank=False, on_delete=models.CASCADE, related_name='jugadorLocal')
    equipoLocal = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE, related_name='equipoLocal')
    golesLocal = models.IntegerField(
        null=True, verbose_name='Numero de goles del equipo local')
    jugadorVisitante = models.ForeignKey(Jugador, null=False, blank=False, on_delete=models.CASCADE, related_name='jugadorVisitante')
    equipoVisitante = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE, related_name='equipoVisitante')
    golesVisitante = models.IntegerField(
        null=True, verbose_name='Numero de goles del equipo local')
    ganador = models.ForeignKey(Jugador, null=False, blank=False, on_delete=models.CASCADE, related_name='ganador')
    class Meta:
        db_table = 'partidos'