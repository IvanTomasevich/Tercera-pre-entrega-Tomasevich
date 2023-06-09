from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import IncidentIssue, UserIssue, AttachIssue
# from .forms import FormularioIssue
from django.urls import reverse, reverse_lazy

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def buscar_usuario(request):
    if request.method == "POST":
        data = request.POST
        buscar = data["buscar"]
        print(buscar)
        users = UserIssue.objects.filter(last_name__icontains=buscar)
        print(users)

        return render(request, 'users.html', {"users": users})


class FormularioCreateTicket(CreateView):
    model = IncidentIssue
    fields = ('tipe', 'level', 'url', 'project')
    success_url = reverse_lazy('v_ticket')


class ViewTicket(ListView):
    model = IncidentIssue
    template_name = 'tickets.html'


class FormularioCreateUser(CreateView):
    model = UserIssue
    fields = ('last_name', 'first_name', 'email', 'cel_phone')
    success_url = reverse_lazy('v_user')


class ViewUser(ListView):
    model = UserIssue
    template_name = 'users.html'
