from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from control.models import Jugador, Equipo, Liga
from control.forms import CargarLiga

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


def cargar_liga(request):
    if request.method == "POST":
        formulario = CargarLiga(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            liga = data["liga"]
            pais= data["pais"]
            liga = Liga(liga=liga, pais=pais)
            # Lo guardan en la Base de datos
            liga.save()

            url_exitosa = reverse('cargar_liga')  # control/liga
            return redirect(url_exitosa)
    else:  # GET
        formulario = CargarLiga()
    http_response = render(
        request=request,
        template_name='control/cargar_liga.html',
        context={'formulario': formulario}
    )
    return http_response

"""
def buscar_cursos(request):
   if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        # cursos = Curso.objects.filter(
        #     Q(nombre=busqueda) | Q(comision__contains=busqueda)
        # )
        contexto = {
            "cursos": cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response
"""