from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def pag_inicio (request):
    http_response = render(
        request=request,
        template_name="inicio.html",
        context={},
    )
    return http_response