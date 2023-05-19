from django import forms
from .models import tipe_incident, level_choices


class FormularioIssue(forms.Form):
    tipe = forms.ChoiceField(label='Tipo de solicitud', choices=(('Incident', 'Incident'), ('Request', 'Request')))
    level = forms.ChoiceField(label='Nivel de prioridad', choices=((1, 'Baja'), (2, 'Media'), (3, 'Alta'), (4, 'Crítica')))
    apellido = forms.CharField(label='Apellido', required=True, max_length=50)
    nombre = forms.CharField(label='Nombre', required=True, max_length=50)
    celular = forms.CharField(label='Numero Cel', max_length=12)
    email = forms.EmailField(label='URL', required=True)
    comentario = forms.CharField(label='Comentario', required=True, widget=forms.Textarea)
    captura_pantalla = forms.ImageField()
