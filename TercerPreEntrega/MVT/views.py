from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import IncidentIssue, UserIssue, AttachIssue
# from .forms import FormularioIssue
from django.urls import reverse, reverse_lazy

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def blog_view(request):
    return render(request, 'blog.html', {})


class FormularioCreateTicket(CreateView):
    model = IncidentIssue
    fields = ('tipe', 'level', 'url', 'project')
    success_url = reverse_lazy('blog')


class ViewTicket(ListView):
    model = IncidentIssue
    template_name = 'blog.html'

class FormularioCreateUser(CreateView):
    model = UserIssue
    fields = ('last_name', 'first_name', 'email', 'cel_phone')
    success_url = reverse_lazy('blog')
