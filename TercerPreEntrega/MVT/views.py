from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'home.html', {})


def about_view(request):
    return render(request, 'about.html', {})


def blog_view(request):
    return render(request, 'blog.html', {})


def contact_view(request):
    return render(request, 'contact.html', {})
