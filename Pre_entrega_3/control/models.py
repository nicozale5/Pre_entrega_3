from django.db import models

# Create your models here.

class Equipo(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    club = models.CharField(max_length=64)
    numero = models.IntegerField()

class Jugador(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    club = models.ManyToManyField(Equipo)

class Atributos(models.Model):
    peso = models.CharField(max_length=32)
    altura = models.CharField(max_length=32)

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
