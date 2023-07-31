from django.db import models

# Se guarda class Equipo y Pais 
"""
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
"""
class Pais(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    altura = models.FloatField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    equipo = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    puntos_por_partido = models.DecimalField(max_digits=4, decimal_places=1)
    asistencias_por_partido = models.DecimalField(max_digits=4, decimal_places=1)
    rebotes_por_partido = models.DecimalField(max_digits=4, decimal_places=1)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

# Se guarda class Atributos y Posicion
"""
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
"""