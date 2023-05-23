"""
URL configuration for TercerPreEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from MVT.views import FormularioCreateTicket, ViewTicket, FormularioCreateUser, ViewUser, buscar_usuario

urlpatterns = [
    path('', views.home_view, name='home'),
    path('user/', FormularioCreateUser.as_view(), name='user'),
    path('buscar_usuario/', buscar_usuario, name='buscar_usuario'),
    path('ticket/', FormularioCreateTicket.as_view(), name='ticket'),
    path('viewTickets/', ViewTicket.as_view(), name='v_ticket'),
    path('viewUsers/', ViewUser.as_view(), name='v_user'),
]
