from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Incident  # UserContact, Attach
from .forms import FormularioIssue
from django.urls import reverse, reverse_lazy

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def blog_view(request):
    return render(request, 'blog.html', {})


def contact_view(request):
    issues = Incident.objects.all()
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


class FormularioCreateTicket(CreateView):
    model = Incident
    fields = ('tipe', 'level', 'url', 'project')
    success_url = reverse_lazy('blog')


class ViewTicket(ListView):
    model = Incident
    template_name = 'blog.html'
