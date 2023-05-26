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
        busqueda = data["busqueda"]
        users = UserIssue.objects.filter(last_name=busqueda)
        contexto = {
            "users": users,
        }
        http_response = render(
            request=request,
            template_name='MVT/users.html',
            context=contexto,
        )
        return http_response


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
