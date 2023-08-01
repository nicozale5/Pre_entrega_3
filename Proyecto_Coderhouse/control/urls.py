from django.contrib import admin
from django.urls import path

from control.views import listar_jugador,listar_equipo


# Urls De Inicio

urlpatterns = [
   path("jugador/", listar_jugador),
   path("equipo/",listar_equipo),
]