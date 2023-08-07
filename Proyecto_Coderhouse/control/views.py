from django.shortcuts import render

from control.models import Jugador, Equipo, Liga

def listar_jugador (request):
    contexto={
        "jugador": Jugador.objects.all(),
    }
    http_response=render(
        request=request,
        template_name="control/listar_jugador.html",
        context=contexto,
    )
    return http_response

def listar_equipo(request):
    contexto = {
        "equipo": Equipo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control/listar_equipo.html',
        context=contexto,
    )
    return http_response

def listar_liga(request):
    contexto = {
        "liga": Liga.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control/listar_liga.html',
        context=contexto,
    )
    return http_response