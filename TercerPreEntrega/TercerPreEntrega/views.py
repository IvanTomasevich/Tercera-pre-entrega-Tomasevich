from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "hola loco"
    response = HttpResponse(saludo)
    return response
