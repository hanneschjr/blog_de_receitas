from django import forms
from .models import Receita

# formulários são classes do Python

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'categoria']