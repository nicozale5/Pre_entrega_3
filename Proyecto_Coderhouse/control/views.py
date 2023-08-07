from django.shortcuts import render

def listar_jugador (request):
    contexto={
        "equipo": "Los Angeles Lakers",
        "jugador": [
            {"nombre": "Tre", "apellido": "Jones", "edad": 23, "posicion": "Base"},
            {"nombre": "Devin", "apellido": "Vassell", "edad": 22, "posicion": "Escolta"},
            {"nombre": "Keldon", "apellido": "Johnson", "edad": 23, "posicion": "Ala"},
            {"nombre": "Jeremy", "apellido": "Sochan", "edad": 20, "posicion": "Ala-Pivot"},
            {"nombre": "Victor", "apellido": "Wembanyama", "edad": 19, "posicion": "Pivot"},
        ]
    }
    http_response=render(
        request=request,
        template_name="control/listar_jugador.html",
        context=contexto,
    )
    return http_response

def listar_equipo(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "equipo": [
            {"nombre": "Los Angeles Lakers", "pais": "Estados Unidos"},
            {"nombre": "Atenas", "pais": "Argentina"},
            {"nombre": "Real Madrid", "pais": "España"},
        ]
    }
    http_response = render(
        request=request,
        template_name='control/listar_equipo.html',
        context=contexto,
    )
    return http_response

def listar_liga(request):
    contexto = {
        "liga": [
            {"nombre": "NBA", "pais": "Estados Unidos"},
            {"nombre": "NCAA", "pais": "Estados Unidos"},
            {"nombre": "ACB", "pais": "España"},
            {"nombre": "Liga Nacional", "pais": "Argentina"},
        ]
    }
    http_response = render(
        request=request,
        template_name='control/listar_liga.html',
        context=contexto,
    )
    return http_response