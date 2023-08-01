from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

"""
def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html
"""

def pag_inicio (request):
    http_response = render(
        request=request,
        template_name="inicio.html",
        context={},
    )
    return http_response