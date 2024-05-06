from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'imagen']

class FormularioRespuesta(forms.Form):
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea(attrs={'rows': 3}))
