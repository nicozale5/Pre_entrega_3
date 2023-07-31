from django.db import models

# Create your models here.

class Equipo(models.Model):
    club = models.CharField(max_length=64)

class Pais(models.Model):
    pais_equipo = [
        ("AR", "Argentina"),
        ("ES", "España"),
        ("US", "Estados Unidos"),
    ]
    name = models.CharField(max_length=60)
    posicion_jugador = models.CharField(max_length=2, choices=pais_equipo)
class Jugador(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    nacionalidad = models.CharField(max_length=256)
    año_debut = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField(null=True)
    club = models.ManyToManyField(Equipo)

class Atributos(models.Model):
    altura = models.FloatField()  # Campo de altura
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # Campo de peso


class Posicion(models.Model):
    posicion_jugador = [
        ("B", "Base"),
        ("E", "Escolta"),
        ("A", "Ala"),
        ("AL", "Ala-Pivot"),
        ("P", "Pivot"),
    ]
    name = models.CharField(max_length=60)
    posicion_jugador = models.CharField(max_length=2, choices=posicion_jugador)
