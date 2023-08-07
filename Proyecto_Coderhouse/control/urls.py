from django.contrib import admin
from django.urls import path

from control.views import (listar_jugador,listar_equipo,listar_liga,cargar_liga,buscar_liga)


# Urls De Inicio

urlpatterns = [
   path("jugador/", listar_jugador,name="Jugador"),
   path("equipo/",listar_equipo,name="Equipo"),
   path("liga/",listar_liga,name="Liga"),
   path("cargar-liga/",cargar_liga, name="cargar_liga"),
   path("buscar-liga/",buscar_liga, name="buscar_liga"),
]