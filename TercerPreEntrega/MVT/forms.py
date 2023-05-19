from django import forms
from .models import tipe_incident, level_choices


class FormularioIssue(forms.Form):
    apellido = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    celular = forms.CharField(max_length=12)
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.Textarea)
    captura_pantalla = forms.ImageField()
    tipe = forms.ChoiceField(choices=tipe_incident)
    level = forms.ChoiceField(choices=level_choices)
