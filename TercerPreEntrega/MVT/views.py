from django.shortcuts import render
from MVT.models import *
from .forms import FormularioIssue

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def blog_view(request):
    return render(request, 'blog.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})


def formulario_view(request):
    if request.method == 'POST':
        form = FormularioIssue(request.POST, request.FILES)
        if form.is_valid():
            # Procesar los datos del formulario
            # Acceder a los campos con form.cleaned_data
            # Guardar la captura de pantalla con form.cleaned_data['captura_pantalla']
            # Redireccionar o mostrar un mensaje de éxito
            pass
    else:
        form = FormularioIssue()

    return render(request, 'contact.html', {'form': form})
