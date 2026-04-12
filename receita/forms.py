from django import forms
from .models import Receita

# formulários são classes do Python

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo').strip()
        if len(titulo) < 3:
            raise forms.ValidationError('O título deve conter pelo menos 3 caracteres.')
        return titulo